import fileinput

x, m = 0, 0
for line in fileinput.input():
    x = 0 if str.isspace(line) else x + int(line)
    m = max(m, x)

print(m)
