import fileinput

l = [0]
for line in fileinput.input():
    if str.isspace(line):
        l.append(0)
    else:
        l[-1] += int(line)

print(sum(sorted(l)[-3:]))
