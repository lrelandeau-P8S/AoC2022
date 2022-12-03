import numpy as np

abc = 'abcdefghijklmnopqrstuvwxyz'
abc += abc.upper()

with open('day3\input.txt', 'r') as file:
    data = file.read().split("\n")

# print(ABC)
# print(len(abc))
# print(data)

result = 0

for contents in data:
    size = len(contents)//2
    cc = ''.join(set(contents[:size]).intersection(contents[size:]))
    result += abc.index(cc) + 1

print(result)