
import numpy as np

with open('day8\input.txt', 'r') as file:
    data = np.array([[*trees] for trees in file.read().split("\n")], dtype=int)

print(data)

scores = np.zeros_like(data)

def find_dist(h,side):
    for k in range(len(side)):
        if h<=side[k]:
            return k+1
    return len(side)

for i in range(len(data)):
    for j in range(len(data)):
        if i==0 or j==0 or i==len(data)-1 or j==len(data[0])-1:
            scores[i,j] = 0
        else:
            distances = []
            side = list(data[:i,j])[::-1]
            distances.append(find_dist(data[i,j],side))

            side = data[i+1:,j]
            distances.append(find_dist(data[i,j],side))
                
            side = list(data[i,:j])[::-1]
            distances.append(find_dist(data[i,j],side))
            
            side = data[i,j+1:]
            distances.append(find_dist(data[i,j],side))
            
            
            scores[i,j] = np.prod(distances)
            # print(data[i,j],distances,scores[i,j])

print(np.max(scores))
