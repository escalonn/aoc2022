import fileinput

score = 0
for line in fileinput.input():
    h, o = line.split()
    his = 'ABC'.index(h)
    outcome = 'XYZ'.index(o)
    score += 1 + outcome * 3 + (his + outcome - 1) % 3

print(score)
