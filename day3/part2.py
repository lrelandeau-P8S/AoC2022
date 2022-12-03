import numpy as np

abc = 'abcdefghijklmnopqrstuvwxyz'
abc += abc.upper()

with open('day3\input.txt', 'r') as file:
    data = file.read().split("\n")

groups = []
for i in range(len(data)//3):
    groups.append(data[i*3:i*3+3])

result = 0

for group in groups:
    cc1 = ''.join(set(group[0]).intersection(group[1]))
    cc = ''.join(set(cc1).intersection(group[2]))
    result += abc.index(cc) + 1

print(result)