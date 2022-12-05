

with open('day4\input.txt', 'r') as file:
    data = [pair.split(",") for pair in file.read().split("\n")]

contained = 0

for pair in data:
    ranges = [elf.split("-") for elf in pair]
    elf0 = ranges[0]
    elf1 = ranges[1]
    if (int(elf0[0]) >= int(elf1[0]) and int(elf0[1]) <= int(elf1[1])) or (int(elf0[0]) <= int(elf1[0]) and int(elf0[1]) >= int(elf1[1])):
        contained += 1
        print(pair)

print(contained)