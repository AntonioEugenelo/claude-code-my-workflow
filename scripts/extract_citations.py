"""Extract and cross-reference all citations in the paper."""
import re, os, collections, sys

sections_dir = sys.argv[1]
active = [
    '11_introduction.tex', '12_related_literature.tex', '13_roadmap.tex',
    '21_general_model.tex', '22_households.tex', '23_firms.tex',
    '24_government.tex', '25_market_clearing_and_gdp.tex', '26_sectoral_tariffs.tex',
    '43_calibration.tex', '55a_benchmark_and_robustness.tex',
    '55b_liberation_day.tex', '55c_sectoral_targeting.tex',
    '60_Conclusions.tex', 'a_appendix.tex',
]

# Match \cite{}, \citep{}, \citet{}
cite_pattern = re.compile(r'\\cite[pt]?\{([^}]+)\}')
all_keys = []
file_keys = collections.defaultdict(list)
# Store context for each citation (the surrounding text)
cite_contexts = collections.defaultdict(list)

for f in active:
    path = os.path.join(sections_dir, f)
    if not os.path.exists(path):
        continue
    text = open(path, 'r', encoding='utf-8').read()
    lines = text.split('\n')
    for line_num, line in enumerate(lines, 1):
        # Skip commented lines
        if line.strip().startswith('%'):
            continue
        matches = cite_pattern.finditer(line)
        for match in matches:
            key_str = match.group(1)
            keys = [k.strip() for k in key_str.split(',')]
            # Get context (surrounding ~80 chars)
            start = max(0, match.start() - 80)
            end = min(len(line), match.end() + 20)
            context = line[start:end].strip()
            for k in keys:
                all_keys.append(k)
                file_keys[k].append(f)
                cite_contexts[k].append((f, line_num, context))

counter = collections.Counter(all_keys)
print('=== CITATION KEYS USED IN PAPER (sorted by frequency) ===')
for k, c in counter.most_common():
    files = sorted(set(file_keys[k]))
    joined = ', '.join(files)
    print(str(c).rjust(3) + ' x ' + k + '  (' + joined + ')')
print()
print('Total unique keys: ' + str(len(counter)))
print('Total citations: ' + str(sum(counter.values())))

# Extract bib keys and titles
bib_path = os.path.join(os.path.dirname(sections_dir), 'bibliography.bib')
bib_text = open(bib_path, 'r', encoding='utf-8').read()
bib_entry_pattern = re.compile(r'^@\w+\{([^,]+),', re.MULTILINE)
bib_keys = set(bib_entry_pattern.findall(bib_text))

cited_keys = set(counter.keys())
unused = bib_keys - cited_keys
missing = cited_keys - bib_keys

print()
print('=== BIB ENTRIES NOT CITED IN PAPER (' + str(len(unused)) + ') ===')
# Get titles for unused entries
title_pattern = re.compile(r'title\s*=\s*\{+([^}]+)\}', re.IGNORECASE)
for k in sorted(unused):
    # Find the entry in bib text
    entry_start = bib_text.find('{' + k + ',')
    if entry_start >= 0:
        entry_end = bib_text.find('\n@', entry_start)
        if entry_end < 0:
            entry_end = len(bib_text)
        entry_text = bib_text[entry_start:entry_end]
        title_match = title_pattern.search(entry_text)
        title = title_match.group(1)[:60] if title_match else '(no title found)'
    else:
        title = '(entry not found)'
    print('  ' + k + ' -- ' + title)

print()
print('=== CITED BUT MISSING FROM BIB (' + str(len(missing)) + ') ===')
for k in sorted(missing):
    files = sorted(set(file_keys[k]))
    print('  ' + k + '  (in: ' + ', '.join(files) + ')')

# Find duplicate bib entries
key_counts = collections.Counter(bib_entry_pattern.findall(bib_text))
dups = {k: v for k, v in key_counts.items() if v > 1}
if dups:
    print()
    print('=== DUPLICATE BIB KEYS ===')
    for k, v in dups.items():
        print('  ' + k + ': appears ' + str(v) + ' times')

# Find semantically duplicate entries (same paper, different keys)
print()
print('=== POTENTIAL SEMANTIC DUPLICATES (same authors, similar titles) ===')
entries = {}
for match in re.finditer(r'@\w+\{([^,]+),\s*(.*?)(?=\n@|\Z)', bib_text, re.DOTALL):
    key = match.group(1)
    body = match.group(2)
    author_match = re.search(r'author\s*=\s*\{([^}]+)\}', body, re.IGNORECASE)
    title_match = title_pattern.search(body)
    year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', body, re.IGNORECASE)
    if author_match and title_match:
        # Normalize author: take last name of first author
        author = author_match.group(1).split(',')[0].split(' and ')[0].strip()
        author = re.sub(r'[{}\\\'"` ]', '', author).lower()
        title = re.sub(r'[{}\\\'"` ]', '', title_match.group(1)).lower()[:40]
        year = year_match.group(1) if year_match else 'unknown'
        entries[key] = (author, title, year)

# Check for duplicates
checked = set()
for k1, (a1, t1, y1) in entries.items():
    for k2, (a2, t2, y2) in entries.items():
        if k1 >= k2:
            continue
        pair = (k1, k2)
        if pair in checked:
            continue
        checked.add(pair)
        if a1 == a2 and y1 == y2 and (t1[:20] == t2[:20] or t1 in t2 or t2 in t1):
            print('  LIKELY DUP: ' + k1 + ' <-> ' + k2)
            print('    ' + k1 + ': ' + a1 + ' (' + y1 + ') "' + t1 + '"')
            print('    ' + k2 + ': ' + a2 + ' (' + y2 + ') "' + t2 + '"')

# Print citation contexts for verification
print()
print('=== CITATION CONTEXTS (for content verification) ===')
for k, c in counter.most_common():
    print()
    print('--- ' + k + ' (cited ' + str(c) + 'x) ---')
    for f, line, ctx in cite_contexts[k][:3]:  # Show up to 3 contexts
        print('  ' + f + ':' + str(line) + '  ...' + ctx + '...')
