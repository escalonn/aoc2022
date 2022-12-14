import fileinput

space = {}
sand = []
active = None

for line in fileinput.input():
    points = [tuple(map(int, p.split(','))) for p in line.split('->')]
    point = points.pop()
    space[point] = '#'
    while points:
        point2 = points.pop()
        step = tuple(c1 != c2 and [-1, 1][c2 - c1 > 0]
                     for c1, c2 in zip(point, point2))
        point_i = tuple(c1 + c2 for c1, c2 in zip(point, step))
        while point_i != point2:
            space[point_i] = '#'
            point_i = tuple(c1 + c2 for c1, c2 in zip(point_i, step))
        space[point_i] = '#'
        point = point2

void = max(y for _, y in space) + 1
done = False

while not done:
    active = 500, 0
    space[active] = 'o'
    while not done:
        for step in [(0, 1), (-1, 1), (1, 1)]:
            candidate = tuple(c1 + c2 for c1, c2 in zip(active, step))
            if candidate[1] >= void:
                done = True
                break
            if candidate not in space:
                del space[active]
                active = candidate
                space[active] = 'o'
                break
        else:
            if not done:
                sand.append(active)
            break

print(len(sand))
