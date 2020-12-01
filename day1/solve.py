#!/usr/bin/env python3
# -------------- PART 1 ----------------
dat = open('input').read().strip().split('\n')
dat = list(map(int, dat))

for i in dat:
  for j in dat:
      if i + j == 2020:
        print(i*j)

# -------------- PART 2 ----------------
for i in dat:
  for j in dat:
    for q in dat:
      
      if q+i + j == 2020:
        print(q*i*j)
