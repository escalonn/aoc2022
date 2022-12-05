import fileinput
from itertools import zip_longest

lines = []

have_lines = False

for line in fileinput.input():
    if not have_lines:
        if not line.isspace():
            lines.append(line)
        else:
            have_lines = True
            t = list(map(list, zip_longest(*lines, fillvalue=' ')))
            stacks = {int(x[-1]): [q for q in x[-2::-1] if not q.isspace()] for x in t[1::4]}
    else:
        words = line.split()
        stacks[int(words[5])].extend(stacks[int(words[3])][-int(words[1]):])
        del stacks[int(words[3])][-int(words[1]):]

print(''.join(v[-1] for k, v in sorted(stacks.items())))
