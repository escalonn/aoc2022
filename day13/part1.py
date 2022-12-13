import fileinput

lines = list(fileinput.input())[::-1]

class Good(Exception): pass
class Bad(Exception): pass

def check(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if l != r:
            raise Good() if l < r else Bad()
    elif isinstance(l, list) and isinstance(r, list):
        i = 0
        while True:
            a, b = i < len(l), i < len(r)
            if not a and b:
                raise Good()
            if not b and a:
                raise Bad()
            if not a and not b:
                break
            check(l[i], r[i])
            i += 1
    else:
        if isinstance(l, int):
            check([l], r)
        else:
            check(l, [r])

s = 0
i = 1

while lines:
    if lines[-1].isspace(): lines.pop()
    l, r = eval(lines.pop()), eval(lines.pop())
    try:
        check(l, r)
    except Good:
        s += i
    except:
        pass
    i += 1

print(s)
