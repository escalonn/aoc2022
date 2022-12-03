import fileinput
from string import ascii_lowercase, ascii_uppercase

x = 0

for line in fileinput.input():
    a, b = line[:len(line) // 2], line[len(line) // 2:]
    both = list(set(a) & set(b))[0]
    if both in ascii_lowercase:
        x += 1 + ascii_lowercase.index(both)
    else:
        x += 27 + ascii_uppercase.index(both)

print(x)
