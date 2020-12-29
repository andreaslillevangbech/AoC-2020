#!/usr/bin/env python3
import re
from collections import Counter
import itertools as it
dat = open('input').read().strip().split('\n')

foods = set()
c = Counter()

pos = {}
for line in dat:
  ing, algs = line.split(" (contains ")
  ing = set(ing.split())
  algs = set(algs[:-1].split(', '))

  foods |= ing
  c.update(ing)

  for alg in algs:
    if alg in pos:
      pos[alg] &= ing
    else:
      pos[alg] = ing.copy()
  
might = set(it.chain.from_iterable(pos.values()))
print(sum(c[food] for food in foods-might))

print("Part 2")
res = []
while True:
  for key, value in pos.items():
    if len(value)==1:
      v = next(iter(value))
      res.append((key, v))
      pos.pop(key)
      for ings in pos.values():
        ings.discard(v)
      break
  else:
    break
assert not pos
res.sort(key = lambda x: x[0])
print(','.join(map(lambda x: x[1], res)))
        

