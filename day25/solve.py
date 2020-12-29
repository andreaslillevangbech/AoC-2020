#!/usr/bin/env python3
import re
from collections import Counter
import itertools as it
pub1 = 13135480
pub2 = 8821721

m = 20201227

def trans(key, sub = 7):
  loop = 1
  val = 1
  while 1:
    val = (val * sub) % m 
    if val == key:
      yield loop
    loop += 1

loop2 = next(trans(pub2))
loop1 = next(trans(pub1))

print(pow(pub2, loop1, m))
print(pow(pub1, loop2, m))

print("yay done")

