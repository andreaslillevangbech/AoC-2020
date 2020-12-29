#!/usr/bin/env python3
import re
import itertools
dat = [14,1,17,0,3,20]
lst = dat[:]

for _ in range(2020-len(lst)):
  if lst[-1] in lst[:-1]:
    prev = list(reversed(lst[:-1])).index(lst[-1]) + 1
    lst.append(prev)
  else:
    lst.append(0)
print(lst[-1])
          
 
print("Part 2")
steps = 30000000

dat = [14,1,17,0,3,20]
last = dat[-1]
lst = {e:i+1 for i,e in enumerate(dat)}

for i in range(len(dat), steps):
  lst[last], last = i, i - lst.get(last,i)
print(last)

