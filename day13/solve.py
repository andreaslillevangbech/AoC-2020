#!/usr/bin/env python3

dat = open('input').read().strip().split('\n')
n, ids = int(dat[0]), dat[1].split(',')
ids = [int(i) for i in ids if i != 'x']

b = min(ids, key=lambda k: -n%k)
print(b * (-n%b))

print("Part 2")
from itertools import count
# Note here I used that the numbers are coprimes such that the lowest common multiple is the product
def p2(smart, **_):
    n = smart[0]
    buses = tuple((i, b) for i, b in enumerate(smart[1]) if isinstance(b, int))
    step = 1
    for i, b in buses:
        n = next(c for c in count(n, step) if (c + i) % b == 0)
        step *= b
    return n
dat = open('input').read().strip().split('\n')
n, ids = int(dat[0]), dat[1].split(',')
ids = [int(i) if i != 'x' else i for i in ids]
print(p2([n,ids]))
