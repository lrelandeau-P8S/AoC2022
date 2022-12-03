import numpy as np

with open('day1\input.txt', 'r') as file: 
    data = [elf.split("\n") for elf in file.read().split("\n\n")]
data = [list(map(int, lst)) for lst in data]

print(max([sum(elf) for elf in data]))