import fileinput

n = 0

for line in fileinput.input():
    pairs = line.split(',')
    a, b, c, d = (int(x) for p in pairs for x in p.split('-'))
    if a == c or a < c and b >= c or c < a and d >= a:
        n += 1

print(n)
