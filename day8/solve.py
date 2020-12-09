#!/usr/bin/env python3
dat = open('input').read().strip().split('\n')

a = 0
visited = []
inst = [x.split() for x in dat]
i=0
now= inst[i]
visited.append(i)
while 1:
  if now[0]=='nop':
    i += 1
  elif now[0]=='acc':
    if now[1][0]=='+':
      a += int(now[1][1:])
    else:
      a -= int(now[1][1:])
    i += 1
  elif now[0]=='jmp':
    if now[1][0]=='+':
      i += int(now[1][1:])
    else:
      i -= int(now[1][1:])
  if i in visited:
    break
  else:
    visited.append(i)
  now = inst[i]
  
print(a)
	

print("Part 2")
print("lenght: ", len(inst))
inst = [x.split() for x in dat]
def run(inn):
  a = 0
  i=0
  now= inn[i]
  visited = []
  visited.append(i)
  while 1:
    if now[0]=='nop':
      i += 1
    elif now[0]=='acc':
      if now[1][0]=='+':
        a += int(now[1][1:])
      else:
        a -= int(now[1][1:])
      i += 1
    elif now[0]=='jmp':
      if now[1][0]=='+':
        i += int(now[1][1:])
      else:
        i -= int(now[1][1:])

    if i in visited:
      return None
    else:
      visited.append(i)

    if i==len(inn):
      return a

    now = inn[i]

for i in range(len(inst)):
  if inst[0]=='acc':
    continue
  new = 'jmp' if inst[0]=='nop' else 'nop'
  inn = inst[:i] + [[new, inst[i][1]]] + inst[i+1:]
  a = run(inn)
  if a:
    print(a)

