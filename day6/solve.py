#!/usr/bin/env python3
dat = open('input').read().strip().split('\n\n')
all = [set(i.replace('\n', '')) for i in dat]
print(sum([len(i) for i in all]))

print("Part 2")
print(sum(len(set.intersection(*map(set, x.split('\n')))) for x in dat))
