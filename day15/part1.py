import fileinput

excluded = set()
beacons = []
# y = 10
y = 2000000

for line in fileinput.input():
    l, r = line.split(':')
    s_text = l[12:]
    sx, sy = [int(a) for a in s_text.split(', y=')]
    b_text = r[24:]
    bx, by = [int(a) for a in b_text.split(', y=')]
    if by == y:
        beacons.append(bx)
    d = abs(sx - bx) + abs(sy - by)
    span = d - abs(sy - y)
    excluded.update(x for x in range(sx - span, sx + span + 1))

excluded.difference_update(beacons)
print(len(excluded))
