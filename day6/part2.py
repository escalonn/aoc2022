import collections
from itertools import islice
import fileinput


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


line = next(fileinput.input())
for i, char in enumerate(sliding_window(line, 14)):
    if len(set(char)) == 14:
        break

print(i + 14)
