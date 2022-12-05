import numpy as np

with open("day2/input.txt", 'r') as ipt:
    data = ipt.read().splitlines()

# print(data)

draws = ['A Y', 'B Y', 'C Y']
wins = ['A Z', 'B Z', 'C Z']
losses = ['A X', 'B X', 'C X']

rocks = ['A Y', 'C Z', 'B X']
papers = ['B Y', 'A Z', 'C X']
scissors = ['C Y', 'B Z', 'A X']

total = 0
for d in data:
    if d in draws:
        total += 3
    elif d in wins:
        total += 6
    if d in rocks:
        total += 1
    if d in papers:
        total += 2
    if d in scissors:
        total += 3

print(total)