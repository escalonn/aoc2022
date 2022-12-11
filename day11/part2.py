import fileinput
from operator import add, mul

lines = list(fileinput.input())[::-1]

monkeys = []
counts = []
ops = {'+': add, '*': mul}

while True:
    lines.pop()
    items = list(map(int, lines.pop()[18:].split(',')))
    text = lines.pop()[23:-1].split()
    op = [ops[text[0]], text[1]]
    div = int(lines.pop().split()[-1])
    yes = int(lines.pop().split()[-1])
    no = int(lines.pop().split()[-1])
    monkeys.append((items, op, div, yes, no))
    counts.append(0)
    if not lines:
        break
    lines.pop()

# multi-modular arithmetic
for items, op, *_ in monkeys:
    for i in range(len(items)):
        items[i] = [items[i] % m[2] for m in monkeys]
    op[1] = None if op[1][0] == 'o' else [int(op[1]) % m[2] for m in monkeys]

for i in range(10000):
    for n, (items, op, div, yes, no) in enumerate(monkeys):
        for old in items:
            new = [op[0](a, b) % m[2] for a, b, m in zip(old, op[1] or old, monkeys)]
            monkeys[[no, yes][new[n] == 0]][0].append(new)
            counts[n] += 1
        items.clear()

counts.sort()
print(counts[-1] * counts[-2])
