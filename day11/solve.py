#!/usr/bin/env python3
dat = open('input').read().strip().split('\n')
dat = [list(line) for line in dat]

def many(lst):
    return "".join("".join(x) for x in lst)
    
prev = dat[:]
n = len(prev)
m = len(prev[0])
while 1:
    nex = [['.' for _ in line] for line in prev]
    for i in range(n):
        for j in range(m):
            occ = 0
            for x in (-1,0,1):
                for y in (-1,0,1):
                    if (0 <= i + x < n and 0 <= j + y < m and (x, y) != (0, 0)):
                        if prev[i+x][j+y]=='#':
                            occ += 1
            if prev[i][j]=='#' and occ>3:
                nex[i][j]='L'
            elif prev[i][j]=='L' and occ==0:
                nex[i][j]='#'
            else:
                nex[i][j] = prev[i][j]

    if nex == prev:
        break
    prev = nex

    
print(many(prev).count('#'))

print("Part 2")
prev = dat[:]
n = len(prev)
m = len(prev[0])
while 1:
    nex = [['.' for _ in line] for line in prev]
    for i in range(n):
        for j in range(m):
            occ = 0
            for x in (-1,0,1):
                for y in (-1,0,1):
                    if (x,y) == (0,0):
                        continue
                    nx = i + x
                    ny = j + y
                    while (0 <= nx < n and 0 <= ny < m and prev[nx][ny]=='.'):
                        nx += x
                        ny += y

                    if (0 <= nx < n and 0 <= ny< m ):
                        if prev[nx][ny]=='#':
                            occ += 1

            if prev[i][j]=='#' and occ>4:
                nex[i][j]='L'
            elif prev[i][j]=='L' and occ==0:
                nex[i][j]='#'
            else:
                nex[i][j] = prev[i][j]

    if nex == prev:
        break
    prev = nex

print(many(prev).count('#'))
