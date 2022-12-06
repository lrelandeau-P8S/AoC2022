with open('day6\input.txt', 'r') as file:
    data = file.read().split("\n")[0]

n=14

# for i in range(len(data)-n):
#     subset = set([c for c in data[i:i+n]])
#     if len(subset) == n:
#         print(i+n)
#         break

print([len(set([c for c in data[i:i+n]])) for i in range(len(data)-n)].index(n)+n)