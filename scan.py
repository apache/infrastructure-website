from pathlib import Path
import re
pattern = re.compile("^\w+:")

for p in Path('content').glob('**/*.md'):
    blanks = 0
    for line in open(p).readlines():
        if line.isspace():
            blanks += 1
            if blanks > 2:
                break
        if blanks > 1 and pattern.match(line):
            print(p)
            print(line,end='')
