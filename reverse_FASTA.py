import os
import sys
import string

# TODO: add argparse
if len(sys.argv) < 3:
    sys.exit('File arguments not fully specified!')
elif not os.path.exists(sys.argv[1]):
    sys.exit('Input file not found!')

with open(sys.argv[1]) as in_file:
    continuous = ''
    for line in in_file:
        if line[0] != '>':
            continuous += line
    continuous = string.replace(continuous, '\n', '')

with open(sys.argv[2], 'w') as out_file:
    inverse = ''
    for i in reversed(continuous):
        inverse += i
    out_file.write(inverse)