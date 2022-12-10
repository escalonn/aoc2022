import fileinput

rope = [(0, 0)] * 10
seen = {rope[-1]}

for line in fileinput.input():
    d, dist = line.split()
    step = (d == 'U') - (d == 'D'), (d == 'R') - (d == 'L')
    for _ in range(int(dist)):
        rope[0] = tuple(map(sum, zip(rope[0], step)))
        for i in range(1, len(rope)):
            if any(abs(a - b) > 1 for a, b in zip(rope[i - 1], rope[i])):
                pull = (max(-1, min(a - b, 1))
                        for a, b in zip(rope[i - 1], rope[i]))
                rope[i] = tuple(map(sum, zip(rope[i], pull)))
        seen.add(rope[-1])

print(len(seen))
