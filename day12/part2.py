import numpy as np
import copy, time
import matplotlib.pyplot as plt

with open('day12\input.txt', 'r') as file:
    data = [[*height] for height in file.read().split("\n")]
# print(data)

abc = [*'abcdefghijklmnopqrstuvwxyz']
starts = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] in ['S','a']:
            starts.append((i+1)*(len(data[0])+2)+(j+1))
            data[i][j] = '0'
        elif data[i][j] == 'E':
            end = (i+1)*(len(data[0])+2)+(j+1)
            data[i][j] = '25'
        else:
            data[i][j] = str(abc.index(data[i][j]))

map = np.array(data, dtype=int)
side = -99
map = np.insert(map, 0, side, axis=0)
map = np.insert(map, len(map), side, axis=0)
map = np.insert(map, 0, side, axis=1)
map = np.insert(map, len(map[0]), side, axis=1)

adjacency = {}
for i in range(len(map)-2):
    i += 1
    for j in range(len(map[0])-2):
        j += 1
        up = [i-1,j]
        down = [i+1,j]
        right = [i,j+1]
        left = [i,j-1]
        possible = [up,down,right,left]
        available = []
        for nei in possible:
            if map[i][j]-map[nei[0]][nei[1]] >= -1 and map[i][j]-map[nei[0]][nei[1]] < 27:
                available.append(nei[0]*len(map[0]) + nei[1])
        if available:
            adjacency[i*len(map[0])+j] = available

min_path = 99999
for start in starts:
    queue = [copy.copy(start)]
    visited = [copy.copy(start)]
    paths = [copy.copy(queue)]
    fig = 1
    while queue:
        id = queue.pop(0)
        if id in adjacency.keys():
            possible = adjacency[id]
            for p in possible:
                if p not in visited:
                    for path in paths:
                        if path[-1] == id:
                            new_path = copy.copy(path)
                            new_path.append(p)
                            paths.append(new_path)
                            queue.append(p)
                            visited.append(p)
    for p in paths:
        if p[-1] == end:
            if len(p)-1 < min_path:
                min_path = len(p)-1
                print(f'Found better path: {min_path}')
print(min_path)