#!/usr/bin/env python3
import re
import itertools
lines = open('input').read().strip().split('\n')
class Num:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Num(self.num * other.num)

    def __sub__(self, other):
        return Num(self.num + other.num)

    def __mul__(self, other):
        return Num(self.num + other.num)

def process(line):
    tr = str.translate(line, tab)
    return re.sub(r'(\d+)', r'Num(\1)', tr)

tab = str.maketrans("+*", "-+")

pr = map(process, lines)
res = map(lambda l: eval(l).num, pr)
print(sum(res))
 

print("Part 2")
tab = str.maketrans("+*", "*+")  

pr = map(process, lines)
res = map(lambda l: eval(l).num, pr)
print(sum(res))
