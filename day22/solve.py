#!/usr/bin/env python3
import re
from collections import Counter
import itertools as it
p1, p2 = open('input').read().strip().split('\n\n')
p1 = [int(x) for x in p1.split('\n')[1:]][::-1]
p2 = [int(x) for x in p2.split('\n')[1:]][::-1]

def combat1(p1, p2):
  while p1 and p2:
    c1, c2 = p1.pop(), p2.pop()
    if c1>c2:
      p1 = [c2, c1] + p1
    else:
      p2 = [c1, c2] + p2

  if p1:
    return sum((i+1)*c for i, c in enumerate(p1))
  elif p2:
    return sum((i+1)*c for i, c in enumerate(p2))
  
print(combat1(p1[:],p2[:]))


print("Part 2")
def combat(p1, p2):
  seen = set()
  while p1 and p2:

    if (tuple(p1), tuple(p2)) in seen:
      return True
    seen.add((tuple(p1), tuple(p2)))

    c1, c2 = p1.pop(), p2.pop()
    if len(p1)>=c1 and len(p2)>=c2:
      win = combat(p1[-c1:], p2[-c2:])
      if win:
        p1.insert(0, c1)
        p1.insert(0, c2)
      else:
        p2.insert(0, c2)
        p2.insert(0, c1)

    else:
      if c1>c2:
        p1.insert(0, c1)
        p1.insert(0, c2)
      else:
        p2.insert(0, c2)
        p2.insert(0, c1)

  return len(p1)>0

combat(p1,p2)
print(sum((i+1)*c for i, c in enumerate(p1)))
    
      
