#!/usr/bin/env python3
dat = open('input.txt').read().strip().split('\n')
dat = [x.split(": ") for x in dat]

sum = 0
for i in dat:
  rule = i[0].split()
  b = rule[0].split('-')
  letter = rule[1]
  low = int(b[0])
  high = int(b[1])
  if letter in i[1]:
    count=0
    for j in i[1]:
      if j==letter:
        count+=1
    if count>=low and count<=high:
      sum+=1

print(sum)
      
print("PART 2")


sum = 0
for i in dat:
  rule = i[0].split()
  b = rule[0].split('-')
  letter = rule[1]
  low = int(b[0])
  high = int(b[1])
  count=0
  if i[1][low-1]==letter:
    count+=1
  if i[1][high-1]==letter:
    count+=1
  if count==1:
    sum+=1

print(sum)
