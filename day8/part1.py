import fileinput

a = list(list(x.strip()) for x in fileinput.input())
b = list(map(list, zip(*a)))

visible = [[False] * len(a[0]) for _ in a]

for i, r in enumerate(a):
    for step in [1, -1]:
        m = '/'
        for j, h in list(enumerate(r))[::step]:
            if h > m:
                visible[i][j] = True
                m = h
for i, r in enumerate(b):
    for step in [1, -1]:
        m = '/'
        for j, h in list(enumerate(r))[::step]:
            if h > m:
                visible[j][i] = True
                m = h

print(sum(v for r in visible for v in r))
