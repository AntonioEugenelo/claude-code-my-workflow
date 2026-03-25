import re, sys

bib_path = "C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/bibliography.bib"
bib_text = open(bib_path, 'r', encoding='utf-8').read()

cited_keys = [
    'baqaee24', 'acemoglu2012', 'Gopinath2020', 'Rubbo2023', 'pasten2020',
    'Baqaee2020', 'Baqaee2023', 'gabaix2011', 'Quintana2024', 'Calvo1983',
    'arce2024caused', 'comin2023', 'ernst2023', 'andrade2023aggregate',
    'Gali2005', 'boehm2023long', 'ecb2009wage', 'kouvavas2021markups',
    'dhyne2006', 'itskhoki2025', 'Gautier2024', 'HUANG_LIU_2004', 'huang2006',
    'Aguilar2025', 'atalay2017important', 'bohringer2021energy', 'christoffel2008new',
    'nakamura2010'
]

# Split bib into entries
entries = re.split(r'\n(?=@)', bib_text)
for key in cited_keys:
    found = False
    for entry in entries:
        if '{' + key + ',' in entry:
            # Extract key info
            title_match = re.search(r'title\s*=\s*\{+([^}]+)\}', entry, re.IGNORECASE)
            author_match = re.search(r'author\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE)
            year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', entry, re.IGNORECASE)
            journal_match = re.search(r'journal\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE)
            title = title_match.group(1) if title_match else '?'
            author = author_match.group(1) if author_match else '?'
            year = year_match.group(1) if year_match else '?'
            journal = journal_match.group(1) if journal_match else '?'
            print(key + ':')
            print('  Title: ' + title[:80])
            print('  Author: ' + author[:60])
            print('  Year: ' + year + '  Journal: ' + journal[:50])
            print()
            found = True
            break
    if not found:
        print(key + ': NOT FOUND IN BIB')
        print()
