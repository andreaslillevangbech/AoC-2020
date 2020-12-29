#!/usr/bin/env python3
dat = open('input.txt').read().strip().split('\n')
dat = sorted([int(x) for x in dat])
dat.append(max(dat)+3)

lst = []
a = 0
for i in dat:
    if i-a>3 or i-a<1:
        print("incompatible")
        break
    lst.append(i-a)
    a = i
print(lst.count(1) *  lst.count(3))

print("Part 2")

dat = [0] + dat
v= {dat[-1]: 1}
for i in reversed(dat[:-1]):
    v[i] = 0
    for key in v:
        if 0<key-i<4:
            v[i] += v[key]
print(v[0])
print(v)
