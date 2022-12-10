import fileinput

head = 0, 0
tail = head
seen = {tail}

for line in fileinput.input():
    d, dist = line.split()
    step = (d == 'U') - (d == 'D'), (d == 'R') - (d == 'L')
    for _ in range(int(dist)):
        head = tuple(map(sum, zip(head, step)))
        if any(abs(h - t) > 1 for h, t in zip(head, tail)):
            pull = (max(-1, min(h - t, 1)) for h, t in zip(head, tail))
            tail = tuple(map(sum, zip(tail, pull)))
            seen.add(tail)

print(len(seen))
