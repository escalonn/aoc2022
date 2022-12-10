import fileinput

x = 1
cycle = 1
screen = []

def tick():
    global cycle
    screen.append('.#'[abs(cycle % 40 - x - 1) <= 1])
    cycle += 1

for line in fileinput.input():
    tick()
    if line[0] == 'a':
        tick()
        x += int(line[5:])
while cycle <= 241:
    tick()

for i in range(6):
    print(''.join(screen[i * 40:(i + 1) * 40]))
