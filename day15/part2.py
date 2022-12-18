import fileinput
from intervaltree import IntervalTree

edge = 4000000
# edge = 20

rows = [IntervalTree() for _ in range(edge + 1)]

for line in fileinput.input():
    l, r = line.split(':')
    s_text = l[12:]
    sx, sy = [int(a) for a in s_text.split(', y=')]
    b_text = r[24:]
    bx, by = [int(a) for a in b_text.split(', y=')]
    d = abs(sx - bx) + abs(sy - by)
    for y in range(max(sy - d, 0), min(sy + d + 1, edge + 1)):
        span = d - abs(sy - y)
        rows[y].addi(sx - span, sx + span + 1)
        rows[y].merge_overlaps(strict=False)

for y, t in enumerate(rows):
    intervals = sorted(t)
    if len(intervals) == 1:
        if intervals[0].begin == 1:
            print(y)
            break
        if intervals[0].end == edge:
            print(edge * edge + y)
            break
    else:
        print(intervals[0].end * edge + y)
        break
