#!/usr/bin/env python3
import re
from collections import Counter
import itertools as it
dat = open('input').read().strip().split('\n')

black = {}
for tile in dat:
  j = None
  x,y = 0,0
  for i in tile:
    if j=='s':
      if i == 'e':
        y-=1
        x+=1
      elif i == 'w':
        y-=1
        x-=1
    elif j == 'n':
      if i == 'e':
        y+=1
        x+=1
      elif i == 'w':
        y+=1
        x-=1

    else:
      if i == 'e':
        x+=2
      if i == 'w':
        x-=2

    j=None
    if i == 's' or i == 'n':
      j = i

  if (x,y) in black:
    del black[(x,y)]
  else:
    black[(x,y)] = True

print(sum(black.values()))        


print("Part 2")
# Fill with White
for x in range(min(map(lambda x: x[0], black.keys())) -2, max(map(lambda x: x[0], black.keys())) +4):
  for y in range(min(map(lambda x: x[1], black.keys())) -1, max(map(lambda x: x[1], black.keys())) +2):
    if (x,y) not in black:
      black[(x,y)] = False

change = {}
for _ in range(100):
  
  # Pad with white
  for loc in change.keys():
    for dx in (-2, -1, 0, 1, 2):
      for dy in (-1, 0, 1):
        if not (loc[0] + dx, loc[1] + dy) in black:
          black[(loc[0] + dx, loc[1] + dy)] = False
          
  change = {}
  for loc, t in black.items():
    cnt = 0
    if t:
      for y in (-1,1):
        for x in (-1,1):
          if (loc[0]+x,loc[1]+y) in black:
            if black[(loc[0]+x,loc[1]+y)]:
              cnt += 1
      for x in (-2,2):
        if (loc[0]+x,loc[1]) in black:
          if black[(loc[0]+x,loc[1])]:
            cnt+=1

      if cnt in (0, 3,4,5,6):
        change[loc] = False
    else:
      for y in (-1,1):
        for x in (-1,1):
          if (loc[0]+x,loc[1]+y) in black:
            if black[(loc[0]+x,loc[1]+y)]:
              cnt += 1
      for x in (-2,2):
        if (loc[0]+x,loc[1]) in black:
          if black[(loc[0]+x,loc[1])]:
            cnt+=1
      if cnt == 2:
        change[loc] = True
      
  for loc, t in change.items():
    black[loc] = t

print(sum(black.values()))        



