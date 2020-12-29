#!/usr/bin/env python3
import re
import itertools
tiles = [tile.split('\n') for tile in open('input').read().strip().split('\n\n')]
tiles = {int(re.findall(r'(\d+)',x[0])[0]): x[1:] for x in tiles}


print("Part 2")
