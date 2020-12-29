#!/usr/bin/env python3
from collections import defaultdict
rules, my, nearby = open('input').read().strip().split('\n\n')
r = defaultdict(list)
for a in rules.split('\n'):
  field, ranges = a.split(': ')
  ranges = ranges.split(' or ')
  for i in ranges:
    l,h = map(int, i.split('-'))
    for j in range(l, h+1):
      r[field].append(j)

near_tickets = nearby.split('\n')[1:]
lst = []
valid_ticket = []
a = set.union(*(set(x) for x in r.values()))
for ticket in near_tickets:
  valid = True
  for val in map(int, ticket.split(',')):
    if val not in a:
      lst.append(val)
      valid = False
  if valid:
    valid_ticket.append(ticket)

print(sum(lst))
      
print("PART 2")
near = [[int(i) for i in x.split(',')] for x in valid_ticket]
mapp = defaultdict(list)
# For each field check if all tickets are in range of a fields rule
for k in r.keys():
  for i in range(len(near[0])):
    if all(ticket[i] in r[k] for ticket in near):
      mapp[k].append(i)

mappp = {}
while any(mapp.values()):
  for field, idx in mapp.items():
    if len(idx)==1:
      mappp[field] = idx[0]
      # remove from other fields
      for rest in mapp.values():
        if mappp[field] in rest:
          rest.remove(mappp[field])
      break

out = 1
myticket = [int(x) for x in my.split('\n')[-1].split(',')]
for k in mappp.keys():
  if k.startswith('departure'):
    out *= myticket[mappp[k]]
print(out)
