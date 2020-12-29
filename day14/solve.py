#!/usr/bin/env python3
import re
import itertools
dat = open('input').read().strip().split('\n')

def part1(prog):
  mask = None
  mem = {}
  for line in dat:
    left, right = line.split(' = ')
    if left.startswith('mask'):
      mask = right
    else:
      addr = re.match("^mem\[(\d+)\]", left).groups()[0]
      arg = f"{int(right):036b}"
      val = ""
      for m, v in zip(mask, arg):
        if m=="X":
          val+=v
        else:
          val+=m
      mem[addr] = int(val,2)
          
  return sum(mem.values())

print(part1(dat))
          
 
print("Part 2")

def get_addr(addr_mask):
    if "X" in addr_mask:
        for r in ("0", "1"):
            for addr in get_addr(addr_mask.replace("X", r, 1)):
                yield addr
    else:
        yield addr_mask

def part2(prog):
  mask = None
  mem = {}
  for line in dat:
    left, right = line.split(' = ')
    if left.startswith('mask'):
      mask = right
    else:
      addr = re.match("^mem\[(\d+)\]", left).groups()[0]
      addr = f"{int(addr):036b}"
      arg = int(right)
      val = ""
      for m, v in zip(mask, addr):
        if m=="X":
          val+=m
        elif m=='0':
          val+=v
        else:
          val+=m
      for i in get_addr(val):
        mem[i] = int(arg)
  return sum(mem.values())
        
print(part2(dat))
    
   
