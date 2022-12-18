from collections import deque
import fileinput
from operator import itemgetter

cubes = set()

for line in fileinput.input():
    cubes.add(tuple(map(int, line.split(','))))

coords = [[*map(itemgetter(i), cubes)] for i in range(3)]
mins = [min(c) - 1 for c in coords]
maxes = [max(c) + 1 for c in coords]

exposed = 0
start = tuple(mins)
visited = {start}
queue = deque([start])

while queue:
    node = queue.pop()
    for i in range(3):
        for s in (-1, 1):
            offset = (s * (i == j) for j in range(3))
            adj = tuple(a + b for a, b in zip(node, offset))
            if adj not in visited and all(a <= b <= c for a, b, c in zip(mins, adj, maxes)):
                if adj in cubes:
                    exposed += 1
                else:
                    queue.appendleft(adj)
                    visited.add(adj)

print(exposed)
