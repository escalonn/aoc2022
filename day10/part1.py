import fileinput

x = 1
cycle = 1
strengths = []

def tick():
    global cycle
    if (cycle - 20) % 40 == 0 and len(strengths) < 6:
        strengths.append(x * cycle)
    cycle += 1

for line in fileinput.input():
    tick()
    if ' ' in line:
        tick()
        x += int(line[5:])
while len(strengths) < 6:
    tick()

print(sum(strengths))
