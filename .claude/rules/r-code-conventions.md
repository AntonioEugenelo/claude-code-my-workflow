---
paths:
  - "**/*.R"
  - "Figures/**/*.R"
  - "scripts/**/*.R"
---

# R Code Standards

**Standard:** Senior Principal Data Engineer + PhD researcher quality

---

## 1. Reproducibility

- `set.seed()` called ONCE at top (YYYYMMDD format)
- All packages loaded at top via `library()` (not `require()`)
- All paths relative to repository root
- `dir.create(..., recursive = TRUE)` for output directories

## 2. Function Design

- `snake_case` naming, verb-noun pattern
- Roxygen-style documentation
- Default parameters, no magic numbers
- Named return values (lists or tibbles)

## 3. Domain Correctness

- Verify IRF computations match Dynare output (sign conventions, scaling)
- Calvo $\theta^p$ = prob of NOT resetting; higher = stickier prices
- IO matrix ordering: $\Omega_X$(buyer-country, seller-country, buyer-sector, seller-sector)
- Country reordering: data (EA=1, USA=2, CHI=3, ROW=4) vs model (EA=1, CHN=2, ROW=3, USA=4)
- Domar weights $\Lambda$ must sum correctly per country
- Trade balance sign: positive = surplus (exports > imports)

## 4. Visual Identity

```r
# --- ECB institutional palette ---
ecb_blue      <- "#003299"
ecb_gold      <- "#FFD700"
ecb_orange    <- "#FF6600"
ecb_green     <- "#009900"
accent_gray   <- "#525252"
negative_red  <- "#b91c1c"
```

### Custom Theme
```r
theme_ecb <- function(base_size = 14) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", color = ecb_blue),
      legend.position = "bottom"
    )
}
```

### Figure Dimensions for Beamer
```r
ggsave(filepath, width = 12, height = 5, bg = "transparent")
```

## 5. RDS Data Pattern

**Heavy computations saved as RDS; slide rendering loads pre-computed data.**

```r
saveRDS(result, file.path(out_dir, "descriptive_name.rds"))
```

## 6. Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Missing `bg = "transparent"` | White boxes on slides | Always include in ggsave() |
| Hardcoded paths | Breaks on other machines | Use relative paths |
| Wrong country index after reorder | IRFs plotted for wrong country | Always map through `new_country_order` |
| Cumulative IRF off-by-one | Cumsum starts from period 0 vs 1 | Verify first-period value matches Dynare |
| Percentage points vs log-deviation | 10x scaling error in IRF plots | Dynare outputs log-deviations; multiply by 100 for pp |
| Energy sector Calvo $\theta=0.01$ | Near-flexible prices treated as sticky | Handle energy sectors separately in analysis |

## 7. Line Length & Mathematical Exceptions

**Standard:** Keep lines <= 100 characters.

**Exception: Mathematical Formulas** -- lines may exceed 100 chars **if and only if:**

1. Breaking the line would harm readability of the math (influence functions, matrix ops, finite-difference approximations, formula implementations matching paper equations)
2. An inline comment explains the mathematical operation:
   ```r
   # Sieve projection: inner product of residuals onto basis functions P_k
   alpha_k <- sum(r_i * basis[, k]) / sum(basis[, k]^2)
   ```
3. The line is in a numerically intensive section (simulation loops, estimation routines, inference calculations)

**Quality Gate Impact:**
- Long lines in non-mathematical code: minor penalty (-1 to -2 per line)
- Long lines in documented mathematical sections: no penalty

## 8. Code Quality Checklist

```
[ ] Packages at top via library()
[ ] set.seed() once at top
[ ] All paths relative
[ ] Functions documented (Roxygen)
[ ] Figures: transparent bg, explicit dimensions
[ ] RDS: every computed object saved
[ ] Comments explain WHY not WHAT
```
