import copy

with open('day7\input.txt', 'r') as file:
    data = file.read().split("\n")

print(data)

class Dir:
    def __init__(self, name, path):
        self.name = name
        self.path = path
    
    def print_all(self):
        print(f'name: {self.name}, \tin dir: {self.path}')

class File:
    def __init__(self, name, size, path):
        self.name = name
        self.size = size
        self.path = path
        
    def print_all(self):
        print(f'name: {self.name}, \tsize: {self.size}, \tdir: {self.path}')

dirs = []
files = []

working_dirs = []

for command in data:
    if command[0] == "$":
        if command[2:4] == "cd":
            print(command[5:], working_dirs)
            if command[5:] == "..":
                # print("go back")
                working_dirs = working_dirs[:-1]
            else:
                working_dirs.append(command[5:])
    elif command[:3] == "dir":
        # print(command[4:])
        dirs.append(Dir(command[4:], ''.join(copy.copy(working_dirs))))
        pass
    else:
        split = command.split(" ")
        files.append(File(split[1], split[0], copy.copy(working_dirs)))

print("========================================")

for d in dirs:
    d.print_all()

for f in files:
    f.print_all()

print("========================================")

dirs_sizes = {"/" : 0}

for dir in dirs:
    size = 0
    dirs_sizes[dir.path+dir.name] = size

print(dirs_sizes)

print("========================================")

for f in files:
    full_path = ''
    for folder in f.path:
        full_path += folder
        dirs_sizes[full_path] += int(f.size)

print(dirs_sizes)

print("========================================")

result = 0
for key in dirs_sizes.keys():
    if dirs_sizes[key] <= 100_000:
        result += dirs_sizes[key]
print(result)