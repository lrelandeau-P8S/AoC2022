
import numpy as np
import matplotlib.pyplot as plt
import copy

with open('day9\input.txt', 'r') as file:
    data = [dir.split(" ") for dir in file.read().split("\n")]

# print(data)

N = 1000
phead = [[N//2,N//2]]
ptail = [[N//2,N//2]]

cphead = [N//2,N//2]
cptail = [N//2,N//2]

for move in data:
    for _ in range(int(move[1])):
        if move[0] == 'R':
            cphead[1] += 1
            if cphead[1]-cptail[1] == 2:
                cptail[1] += 1
                if cphead[0]-cptail[0] == 1:
                    cptail[0] += 1
                elif cphead[0]-cptail[0] == -1:
                    cptail[0] -= 1

        elif move[0] == 'L':
            cphead[1] -= 1
            if cphead[1]-cptail[1] == -2:
                cptail[1] -= 1
                if cphead[0]-cptail[0] == 1:
                    cptail[0] += 1
                elif cphead[0]-cptail[0] == -1:
                    cptail[0] -= 1

        elif move[0] == 'U':
            cphead[0] -= 1
            if cphead[0]-cptail[0] == -2:
                cptail[0] -= 1
                if cphead[1]-cptail[1] == 1:
                    cptail[1] += 1
                elif cphead[1]-cptail[1] == -1:
                    cptail[1] -= 1

        elif move[0] == 'D':
            cphead[0] += 1
            if cphead[0]-cptail[0] == 2:
                cptail[0] += 1
                if cphead[1]-cptail[1] == 1:
                    cptail[1] += 1
                elif cphead[1]-cptail[1] == -1:
                    cptail[1] -= 1

        phead.append(copy.copy(cphead))
        ptail.append(copy.copy(cptail))

plt.figure()
headplot = np.zeros(shape=(N,N))
for pos in phead:
    headplot[pos[0],pos[1]] = 255
plt.imshow(headplot, interpolation='nearest', cmap='Greys')

plt.figure()
tailplot = np.zeros(shape=(N,N))
for pos in ptail:
    tailplot[pos[0],pos[1]] = 255
plt.imshow(tailplot, interpolation='nearest', cmap='Greys')

print(np.count_nonzero(tailplot))

# plt.show()