#!/usr/bin/env python3

dat = open('input').read().strip().split('\n')
dat = [int(x) for x in dat]
for i, el in enumerate(dat):
  if i < 25:
    continue
  cnt = False
  qu = dat[i-25:i]
  for j in qu:
    for q in qu:
      if j!=q:
        if j+ q==el:
          cnt = True
  if not cnt:
    here = el
    print(el)
    break

print("Part 2")
series = [0]
for x in dat:
	series.append(x + series[-1])
for i in range(len(dat)):
  j = i+2
  while j < len(dat) and series[j]-series[i] <= here:
    if series[j] - series[i] == here:
      print(max(dat[i:j])+min(dat[i:j]))
      break
    j += 1
    

