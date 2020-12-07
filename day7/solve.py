#!/usr/bin/env python3
import re
import collections
dat = open('input').read().strip().split('\n')

containedin = collections.defaultdict(set)
contains = collections.defaultdict(list)
for line in dat:
  color = re.match(r'(.+?) bags contain', line)[1]
  for cnt, innercolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
    cnt = int(cnt)
    containedin[innercolor].add(color)
    contains[color].append((cnt, innercolor))

holdsgold = set()
def check(color):
    for c in containedin[color]:
        holdsgold.add(c)
        check(c)
check('shiny gold')
print(len(holdsgold))

print("Part 2")
def holds(color):
  cnt = 0
  for number, bag in contains[color]:
    cnt += number
    cnt += number*holds(bag)
  return cnt
print(holds('shiny gold'))
