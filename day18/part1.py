import math
import fileinput

cubes = []
exposed = 0

for line in fileinput.input():
    cube = tuple(map(int, line.split(',')))
    exposed += 6
    for other in cubes:
        if 2 == math.prod(abs(c1 - c2) + 1 for c1, c2 in zip(cube, other)):
            exposed -= 2
    cubes.append(cube)

print(exposed)
