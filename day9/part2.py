import numpy as np
import matplotlib.pyplot as plt
import copy, math

with open('day9\input.txt', 'r') as file:
    data = [dir.split(" ") for dir in file.read().split("\n")]

# print(data)

N = 1000
positions = []
rope = []
size = 10
for i in range(size):
    positions.append([])
    positions[i].append([N//2,N//2])
    rope.append([N//2,N//2])

def update():
    vect = np.array(rope[i])-np.array(rope[i+1])
    dist = np.linalg.norm(vect)
    
    if (abs(vect[0]) == 2 and vect[1]==0) or (abs(vect[1]) == 2 and vect[0]==0):
        options = [copy.copy(rope[i]), copy.copy(rope[i]), copy.copy(rope[i]), copy.copy(rope[i])]
        options[0][0] += 1
        options[1][0] -= 1
        options[2][1] += 1
        options[3][1] -= 1
        dists = [np.linalg.norm(np.array(rope[i+1])-np.array(option)) for option in options]
        ind = dists.index(min(dists))
        rope[i+1] = copy.copy(options[ind])
    elif dist>2.23:
        rope[i+1][0] += vect[0]//abs(vect[0])
        rope[i+1][1] += vect[1]//abs(vect[1])

for l, move in enumerate(data):
    for _ in range(int(move[1])):
        for i in range(size-1):
            if move[0] == 'R':
                if i == 0:
                    rope[i][1] += 1
                update()

            elif move[0] == 'L':
                if i == 0:
                    rope[i][1] -= 1
                update()

            elif move[0] == 'U':
                if i == 0:
                    rope[i][0] -= 1
                update()

            elif move[0] == 'D':
                if i == 0:
                    rope[i][0] += 1
                update()
    
            if i==0:
                positions[i].append(copy.copy(rope[i]))
            positions[i+1].append(copy.copy(rope[i+1]))
    
        # if l == 1:
        #     plt.figure()
        #     ropeplot = np.zeros(shape=(N,N))
        #     for r in rope:
        #         ropeplot[r[0],r[1]] = 255
        #     plt.imshow(ropeplot, interpolation='nearest', cmap='Greys')

plt.figure()
headplot = np.zeros(shape=(N,N))
for pos in positions[0]:
    headplot[pos[0],pos[1]] = 255
plt.imshow(headplot, interpolation='nearest', cmap='Greys')

plt.figure()
tailplot = np.zeros(shape=(N,N))
for pos in positions[-1]:
    tailplot[pos[0],pos[1]] = 255
plt.imshow(tailplot, interpolation='nearest', cmap='Greys')

print(np.count_nonzero(tailplot))

# plt.show()