import fileinput

lines = list(fileinput.input())[::-1]

monkeys = []
counts = []

while True:
    lines.pop()
    items = list(map(int, lines.pop()[18:].split(',')))
    src = lines.pop()[19:]
    div = int(lines.pop().split()[-1])
    yes = int(lines.pop().split()[-1])
    no = int(lines.pop().split()[-1])
    monkeys.append((items, src, div, yes, no))
    counts.append(0)
    if not lines:
        break
    lines.pop()

for _ in range(20):
    for n, (items, src, div, yes, no) in enumerate(monkeys):
        for old in items:
            new = eval(src) // 3
            monkeys[[no, yes][new % div == 0]][0].append(new)
            counts[n] += 1
        items.clear()

counts.sort()
print(counts[-1] * counts[-2])
