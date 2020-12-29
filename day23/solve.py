#!/usr/bin/env python3
import re
from collections import Counter
import itertools as it
dat = 952438716
cups = [int(x) for x in str(dat)]

N = 10
steps = N*10

def dest(cup, sub):
  if cup == 1:
    cup = N
  if cup-1 in sub:
    return dest(cup-1, sub)
  return cup - 1

def action(cups):
  sub = [cups.pop(1) for _ in range(3)]
  cup = dest(cups[0], sub)
  idx = cups.index(cup)
  cups[idx+1:idx+1] = sub
  cups.append(cups.pop(0))
  return cups
  
for _ in range(steps):
  cups = action(cups)

print(cups)

idx = cups.index(1)
lst = cups[idx+1:] + cups[:idx]
print(''.join(map(str,lst)))


print("Part 2")
N = 1000000
steps = N*10

def dest(cup, sub):
  if cup == 1:
    cup = N+1
  if cup-1 in sub:
    return dest(cup-1, sub)
  return cup - 1

cups = [int(x) for x in str(dat)]
for i in range(max(cups)+1, N+1):
  cups.append(i)
dic = {}
prev = cups[-1]
for i in cups:
  dic[prev] = i
  prev = i
start = cups[0]

for _ in range(steps):
  a = dic[start]
  b = dic[a]
  c = dic[b]
  d = dic[c]
  # Remove a,b,c from list
  dic[start] = d
  # Get destination
  new = dest(start ,[a,b,c])
  dic[c] = dic[new]
  dic[new] = a
  start = dic[start]

print(dic[1] * dic[dic[1]])


