import numpy as np

with open('day5\input.txt', 'r') as file:
    data = file.read().split("\n")

size = len(data[0])
n = 9 # size = 4n - 1

for i, packet in enumerate(data):
    if packet[:2] == " 1":
        splitAt = i

start = data[:splitAt]
cols = []
for _ in range(n):
    cols.append([])

print(start)

for i, row in enumerate(start):
    for j in range(n):
        crate = row[j*3+j:j*4+3]
        if crate != '   ':
            cols[j].append(crate)


moves = data[splitAt+2:]
moves = [move.split(" ") for move in moves]

print(cols)
print(moves)

for move in moves:
    quantity = int(move[1])
    fromPile = int(move[3]) - 1
    toPile = int(move[5]) - 1
    print(quantity, fromPile, toPile)
    for _ in range(quantity):
        cols[toPile].insert(0, cols[fromPile].pop(0))

print(cols)

output = ''
for c in cols:
    output += c[0][1:-1]

print(output)