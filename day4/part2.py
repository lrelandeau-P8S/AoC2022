

with open('day4\input.txt', 'r') as file:
    data = [pair.split(",") for pair in file.read().split("\n")]

overlap = 0

for pair in data:
    ranges = [elf.split("-") for elf in pair]
    elf0 = [int(r) for r in ranges[0]]
    elf1 = [int(r) for r in ranges[1]]
    if (elf0[0] >= elf1[0] and elf0[0] <= elf1[1]) or (elf0[1] >= elf1[0] and elf0[1] <= elf1[1]) or (elf1[0] >= elf0[0] and elf1[0] <= elf0[1]) or (elf1[1] >= elf0[0] and elf1[1] <= elf0[1]):
        overlap += 1
        print(pair)

print(overlap)