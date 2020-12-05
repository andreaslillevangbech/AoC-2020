#!/usr/bin/env python3
dat = open('input').read().strip().split('\n\n')
dat = [i.replace("\n", " ") for i in dat]
    
fields = """byr 
iyr 
eyr 
hgt 
hcl 
ecl 
pid 
cid""".split('\n') 
fields = [i.strip() for i in fields]

count = 0
for i in dat:
  f = fields[:]
  for d in i.split():
    key, value = d.split(":")
    if key in f:
      f.remove(key)
  if len(f)==0 or f==['cid']:
    count+=1
print(count)

print(" PART 2 " )

import re

def check_height(x):
    if m := re.match(r'^(\d{1,})(cm|in)$', x):
        if m[2] == 'cm' and 150 <= int(m[1]) <= 193:
            return True
        elif m[2] == 'in' and 59 <= int(m[1]) <= 76:
            return True
    return False

count = 0
for i in dat:
  f = fields[:]
  valid = True
  for d in i.split():
    key, value = d.split(":")
    if key == 'byr':
      if not 1920 <= int(value) <= 2002:
        valid = False
    elif key == 'iyr':
      if not 2010 <= int(value) <= 2020:
        valid = False
    elif key == 'eyr':
      if not 2020 <= int(value) <= 2030:
        valid = False
    elif key == 'hgt':
      if not check_height(value):
        valid = False
    elif key=='hcl':
        if not re.match(r'#[a-f0-9]{6}', value):
          valid = False
    elif key=='ecl':
      if not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        valid = False
    elif key == 'pid':
      if not (len(value)==9 and value.isdigit()): 
        valid  = False
    if key in f:
      f.remove(key)
  if len(f)==0 or f==['cid']:
    if valid:
      count+=1
print(count)
