import fileinput
import math

a = list(list(x.strip()) for x in fileinput.input())

best = 0

for i, r in enumerate(a):
    for j, h in enumerate(r):
        d = []
        for s in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            i2, j2 = i, j
            d.append(0)
            while (0 <= (i2 := i2 + s[0]) < len(a) and
                   0 <= (j2 := j2 + s[1]) < len(r)):
                d[-1] += 1
                if a[i2][j2] >= h:
                    break
        best = max(best, math.prod(d))

print(best)
