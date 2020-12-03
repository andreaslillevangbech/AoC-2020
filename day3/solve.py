#!/usr/bin/env python3
dat = open('input').read().strip().split('\n')
h = len(dat)
w = len(dat[0])
count = 0
for i in range(h):
  j = i*3 % w
  if dat[i][j] == '#':
    count+=1
print(count)

print("Part 2")
def tree(x):
  count = 0
  for i in range(0, h, x[1]):
    j = (i//x[1])*x[0] % w
    if dat[i][j] == '#':
      count+=1
  return count

slopes = [(1,1), (3,1), (5,1), (7,1) ,(1,2)]
lst = map(tree, slopes)
p=1
for i in lst:
  p *= i
print(p)
