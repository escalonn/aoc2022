import fileinput

n = 0

for line in fileinput.input():
    pairs = line.split(',')
    a, b, c, d = (int(x) for p in pairs for x in p.split('-'))
    if c <= a and d >= b or a <= c and b >= d:
        n += 1

print(n)
