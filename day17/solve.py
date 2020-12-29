#!/usr/bin/env python3
import re
import itertools
from tqdm import tqdm
dat = open('input').read().strip().split('\n')

grid = {}
for i, line in enumerate(dat):
  for j, ch in enumerate(line):
    grid[(i, j, 0, 0)] = ch == '#'

def cycle(grid):
  new = {}
  # check each point in grid
  for x in range(min(k[0] for k in grid.keys()) -1, max(k[0] for k in grid.keys()) +2):
    for y in range(min(k[1] for k in grid.keys()) -1, max(k[1] for k in grid.keys()) +2):
      for z in range(min(k[2] for k in grid.keys()) -1, max(k[2] for k in grid.keys()) +2):
        for w in range(min(k[3] for k in grid.keys()) -1, max(k[3] for k in grid.keys()) +2):
          act = grid.get((x,y,z,w), 0)
          # loop over 26 neighbors
          a = 0
          for dx, dy, dz, dw in itertools.product((-1,0,1), repeat=4):
            if (dx, dy, dz, dw) == (0,0,0,0):
              continue
            if grid.get((x+dx, y+dy, z+dz, w+dw), 0): 
              a += 1
          # Apply rules
          if (act and a in (2,3)) or (not act and a == 3):
            new[(x,y,z,w)] = 1
  return new
          
for _ in range(6):
  print(sum(grid.values()))
  grid = cycle(grid)
print(sum(grid.values()))
          


        
    
    
    
          
 
print("Part 2")
