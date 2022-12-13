import fileinput
from functools import cmp_to_key
from itertools import zip_longest

dividers = [[[2]], [[6]]]
packets = [eval(x) for x in fileinput.input() if not x.isspace()] + dividers

def cmp(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return l - r
    elif isinstance(l, list) and isinstance(r, list):
        for a, b in zip_longest(l, r):
            if a is None: return -1
            if b is None: return 1
            c = cmp(a, b)
            if c != 0: return c
        return 0
    else:
        if isinstance(l, int):
            return cmp([l], r)
        else:
            return cmp(l, [r])

packets.sort(key=cmp_to_key(cmp))

print((packets.index(dividers[0]) + 1) * (packets.index(dividers[1]) + 1))
