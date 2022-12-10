
import numpy as np
import matplotlib.pyplot as plt
import copy

with open('day10\input.txt', 'r') as file:
    data = [dir.split(" ") for dir in file.read().split("\n")]

# print(data)

log = []
start = 20
div = 40
ck_cnt = 0
reg = 1

def IncNCheck():
    global ck_cnt
    ck_cnt += 1
    if (ck_cnt-start)%40 == 0:
        log.append([ck_cnt, reg])

for op in data:
    IncNCheck()
    if op[0] == 'addx':
        IncNCheck()
        reg += int(op[1])

print(sum([np.prod(np.array(entry)) for entry in log]))