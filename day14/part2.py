"""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

import numpy as np
import time

below = np.array([1,0])
leftD = np.array([1,-1])
rightD = np.array([1,1])

def add_sand(cave):
    try:
        spawn = np.asarray(np.where(cave == "+")).T[0]
    except IndexError:
        return cave, False    
    pos = spawn
    stopped = True
    while stopped:
        try:
            if cave[tuple(pos+below)] == '.':
                pos += below
            elif cave[tuple(pos+leftD)] == '.':
                pos += leftD
            elif cave[tuple(pos+rightD)] == '.':
                pos += rightD
            else:
                cave[tuple(pos)] = 'o'
                stopped = False
        except IndexError:
            return cave, False
    return cave, True

with open('day14\input.txt', 'r') as file:
    data = [[[int(r) for r in rock.split(",")] for rock in rocks.split(" -> ")] for rocks in file.read().split("\n")]
# print(data)

minx = 0
maxx = 0
miny = 500
maxy = 500
for rocks in data:
    for rock in rocks:
        if int(rock[0]) < miny:
            miny = int(rock[0])
        if int(rock[0]) > maxy:
            maxy = int(rock[0])
        if int(rock[1]) > maxx:
            maxx = int(rock[1])
floor = 2
extend = maxx - minx
cave = np.full(shape=(maxx-minx+1+floor,maxy-miny+1+2*extend), fill_value=".", dtype=str)
# print(np.array2string(cave, separator=' ', formatter={'str_kind': lambda x: x}))

for rocks in data:
    for i in range(len(rocks)-1):
        xs = sorted([rocks[i][1], rocks[i+1][1]])
        ys = sorted([rocks[i][0]-miny+extend, rocks[i+1][0]-miny+extend])
        cave[xs[0]:xs[1]+1, ys[0]:ys[1]+1] = '#'
pour_point = [0, 500-miny+extend]
cave[pour_point[0], pour_point[1]] = "+"
cave[-1] = '#'

fall = True
cnt = 0
while fall:
    cave, fall = add_sand(cave)
    if fall:
        cnt += 1
np.savetxt('day14/cave2.txt', cave, fmt="%s")
print(cnt)