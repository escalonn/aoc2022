import fileinput
from string import ascii_lowercase, ascii_uppercase

x = 0
lines = []
for line in fileinput.input():
    lines.append(line.rstrip())
for group in [lines[i:i + 3] for i in range(0, len(lines), 3)]:
    both = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
    if both in ascii_lowercase:
        x += 1 + ascii_lowercase.index(both)
    else:
        try:
            x += 27 + ascii_uppercase.index(both)
        except:
            print(both)

print(x)
