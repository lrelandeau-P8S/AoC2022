
import numpy as np

with open('day8\input.txt', 'r') as file:
    data = np.array([[*trees] for trees in file.read().split("\n")], dtype=int)

# print(data)

visible = np.zeros_like(data)

for i in range(len(data)):
    for j in range(len(data)):
        if i==0 or j==0 or i==len(data)-1 or j==len(data[0])-1:
            visible[i,j] = True
        else:
            side = data[:i,j]
            if all(np.ones_like(side)*data[i,j] > side):
                visible[i,j] = True

            side = data[i+1:,j]
            if all(np.ones_like(side)*data[i,j] > side):
                visible[i,j] = True
                
            side = data[i,:j]
            if all(np.ones_like(side)*data[i,j] > side):
                visible[i,j] = True
            
            side = data[i,j+1:]
            if all(np.ones_like(side)*data[i,j] > side):
                visible[i,j] = True
            
            # print(side)

print(visible)
print(sum(np.ndarray.flatten(visible)))
