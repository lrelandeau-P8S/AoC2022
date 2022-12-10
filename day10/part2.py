
import numpy as np
import matplotlib.pyplot as plt
import copy, time

with open('day10\input.txt', 'r') as file:
    data = [dir.split(" ") for dir in file.read().split("\n")]

# print(data)

start = 20
div = 40
ck_cnt = 0
reg = 1

screen = np.zeros((6,40))

def IncNCheck():
    global ck_cnt
    ck_cnt += 1
    row = ck_cnt//div
    pos = ck_cnt%div -1
    if pos in [reg-1, reg, reg+1]:
        screen[row,pos] = 1

for op in data:
    IncNCheck()
    if op[0] == 'addx':
        IncNCheck()
        reg += int(op[1])

plt.figure()
plt.imshow(screen, interpolation='nearest', cmap='Greys')
plt.show()