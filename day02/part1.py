import fileinput

score = 0
for line in fileinput.input():
    h, m = line.split()
    his = 'ABC'.index(h)
    mine = 'XYZ'.index(m)
    score += 1 + mine
    if his == (mine - 1) % 3:
        score += 6
    elif his == mine:
        score += 3

print(score)
