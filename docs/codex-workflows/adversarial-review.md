# Adversarial Review Loop

Use this workflow when the user asks for a harsh review, an adversarial pass, a devil's-advocate pass, or a deep external-style review loop.

When the Codex client supports repo-local hooks, this workflow also has hook-backed enforcement for active review completeness and unresolved reviewer-conflict state through `.codex/config.toml` and `.codex/hooks/stop_review_enforcer.py`.

## Goal

Reproduce the old multi-agent review loop as closely as Codex allows:

1. route the target to the right review agents
2. run the baseline review agents in the right waves
3. add a hostile challenge pass
4. fix locally
5. verify
6. re-run the required review agents

The loop is intentionally not fully auto-resolving. If reviewer sets produce materially incompatible directions, stop and ask the user to settle the disagreement before implementing further fixes.

## Read-Only Rule

All review agents must be spawned as read-only Codex `explorer` agents.

- No review agent edits files.
- No review agent gets file ownership.
- No review agent is asked to implement fixes.

## Workflow

### Step 1: Plan the Round

Run:

```bash
python scripts/review_plan.py path/to/target --round 1 --adversarial
```

This prints the document type, required review agents, execution waves, and adversarial challenge phase.

### Step 2: Start Tracking

Run:

```bash
./scripts/review-mode.sh start "path/to/target" 1 adversarial
```

Mark each completed review agent with:

```bash
./scripts/review-mode.sh mark proofreader
```

If reviewer sets reach a material disagreement that needs user adjudication, record it immediately:

```bash
./scripts/review-mode.sh conflict "narrative-reviewer wants compression; theory-critic requires caveats that change the framing"
```

After the user settles the disagreement, clear it with:

```bash
./scripts/review-mode.sh resolve
```

If hooks are active, the Stop hook will keep the turn open while required review agents are still missing or a reviewer conflict remains recorded.

### Step 3: Run the Baseline Review Agents

Spawn the required review agents as `explorer` agents, using the prompt cards in `.codex/review_agents/`.

For papers, the default round-one baseline matches the old routing:

`proofreader ∥ derivation-auditor ∥ figure-reviewer → theory-critic → narrative-reviewer`

### Step 4: Run the Adversarial Challenge Pass

Use `devils-advocate` after the baseline review set has established the main weaknesses.

The challenge pass should produce the hardest unresolved objections, not re-state every proofreader issue.

### Step 5: Check For Material Reviewer Disagreement

After each review wave, compare the reviewer findings before editing.

Stop and ask the user to choose a direction when reviewer sets disagree in a way that would materially change the implementation. Examples:

- one set wants a shorter, cleaner argument while another requires more caveats or setup
- one set wants structural compression while another wants additional exposition or signposting
- one set supports a framing change that another says would overstate, misstate, or weaken the claim

Do not stop for minor differences in emphasis, severity, or wording. Stop when the disagreement changes what should be written next.

### Step 6: Fix Locally

The main agent integrates the findings, edits the files, and verifies outputs.

### Step 7: Re-Plan the Next Round

Run:

```bash
python scripts/review_plan.py path/to/target --round 2 --adversarial
```

Round 2+ drops round-one-only agents unless you explicitly choose to rerun them.

### Step 8: Stop Conditions

Stop when one of the following is true:

- no critical findings remain
- the requested review threshold is met, for example `>= 90/100` from every involved review agent
- review-agent sets have reached a material disagreement that requires user adjudication
- the same blocking verification failure occurs twice
- five fix-review rounds have been exhausted

## Output Discipline

- Save review artifacts under `quality_reports/reviews/` when the task calls for on-disk reports.
- Use findings-first output.
- Separate blocking findings from challenge questions and from optional polish.

## Suggested Aggregation File

For large reviews, create an aggregate run note using `templates/adversarial-review-report.md`.
