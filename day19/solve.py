#!/usr/bin/env python3
import re
import itertools
rules, mess = open('input').read().strip().split('\n\n')
rules = [x.split(': ') for x in rules.split('\n')]
rules = {x[0]: x[1] for x in rules}

def parse(num):
  if num == '8':
    return parse('42') + '+'
  elif num == '11':
    a =parse('42')
    b =parse('31')
    return '(?:' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 100)) + ')'

  rule = rules[num]
  if '"' in rule:
    return rule[1]
  else:
    parts = rule.split(' | ')
    res = []
    for part in parts:
      ns = part.split(' ')
      res.append(''.join(parse(n) for n in ns))
    return '(?:' + '|'.join(res) + ')'
  
z = parse('0')
print(z)
ct = 0
for m in mess.split('\n'):
  ct += bool(re.fullmatch(z, m))
print(ct) 

print("Part 2")
z = parse('0')
ct = 0
for m in mess.split('\n'):
  ct += bool(re.fullmatch(z, m))
print(ct) 

