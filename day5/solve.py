#!/usr/bin/env python3
dat = open('input').read().strip().split('\n')

id = []
for i in dat:
  a = i[:-3].replace("F","0").replace("B","1")
  b = i[-3:].replace("R","1").replace("L","0")
  id.append(int(a,2)*8 + int(b,2))

ids = [int( i.replace('F','0').replace('B','1').replace('R','1').replace('L','0'),2) for i in dat]
  
print(max(id))
print(max(ids))

print("Part 2")
lst = [i for i in range(min(ids), max(ids)) if not i in ids]

print(lst)
