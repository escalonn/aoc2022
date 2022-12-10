import fileinput

lines = list(reversed(list(fileinput.input())))
fs = {}
pwd = [fs]

while lines:
    tokens = lines.pop().split()
    if tokens[1] == 'cd':
        if tokens[2] == '/':
            pwd = [fs]
        elif tokens[2] == '..':
            pwd.pop()
        else:
            pwd.append(pwd[-1][tokens[2]])
        continue
    while lines and lines[-1][0] != '$':
        tokens = lines.pop().split()
        if tokens[0] == 'dir':
            pwd[-1][tokens[1]] = {}
        else:
            pwd[-1][tokens[1]] = int(tokens[0])


size = {}

def traverse(node, name):
    size[name] = 0
    for k, v in node.items():
        if isinstance(v, int):
            size[name] += v
        else:
            size[name] += traverse(v, name + '/' + k)
    return size[name]

traverse(fs, '/')

target = 30000000 - (70000000 - size['/'])
print(min(x for x in size.values() if x >= target))
