#!/usr/bin/env python3
import re

dat = open('input').read().strip().split('\n')
dat = [(x[0], int(x[1:])) for x in dat]

x,y = 0,0
d = 0
for line in dat:
    if line[0]=='N':
        y += line[1]
    if line[0]=='S':
        y-= line[1]
    if line[0]=='E':
        x += line[1]
    if line[0]=='W':
        x-= line[1]
    if line[0] == 'R':
        d -= line[1]
    if line[0] == 'L':
        d+= line[1]
    if line[0] == 'F':
        if d % 360 == 90:
            y += line[1]
        elif d % 360 == 180:
            x -= line[1]
        elif d % 360 == 270:
            y -= line[1]
        else:
            x += line[1]
print(abs(x) + abs(y))


print("Part 2")

x,y = 0,0
dx, dy = 10, 1
for line in dat:
    arg = line[1]
    if line[0]=='N':
        dy += line[1]
    if line[0]=='S':
        dy-= line[1]
    if line[0]=='E':
        dx += line[1]
    if line[0]=='W':
        dx-= line[1]
    if line[0] == 'R':
        while arg:
            dx, dy = dy, -dx
            arg -= 90
    if line[0] == 'L':
        while arg:
            dx, dy = -dy, dx
            arg  -= 90
    if line[0] == 'F':
        x += dx*line[1]
        y += dy*line[1]
print(abs(x) + abs(y))
