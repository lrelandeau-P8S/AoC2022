import numpy as np

with open("day2/input.txt", 'r') as ipt:
    data = ipt.read().splitlines()

# print(data)

draws = ['A X', 'B Y', 'C Z']
wins = ['A Y', 'B Z', 'C X']
losses = ['A Z', 'B X', 'C Y']

total = 0
for d in data:
    if d in draws:
        total += 3
    elif d in wins:
        total += 6

data_flat = list(np.ndarray.flatten(np.array([d.split(' ') for d in data])))
count_rocks = data_flat.count('X')
count_paper = data_flat.count('Y')
count_scissors = data_flat.count('Z')

print(total + count_rocks + count_paper*2 + count_scissors*3)