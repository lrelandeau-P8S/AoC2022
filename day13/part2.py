import functools, ast

with open('day13\input.txt', 'r') as file:
    data = file.read().split("\n")
while '' in data:
    data.remove('')
p1 = '[[2]]'
p2 = '[[6]]'
data.append(p1)
data.append(p2)

def compare(first, second):
    l = max(len(first),len(second))
    for j in range(l):
        if len(first)!=len(second):
            try:
                dummy = second[j]
            except IndexError:
                return -1
            try:
                dummy = first[j]
            except IndexError:
                return 1
        if type(first[j]) == type(second[j]):
            if type(first[j]) is list:
                out = compare(first[j], second[j])
                if out == 1: 
                    return 1
                elif out == -1:
                    return -1
            if type(first[j]) is int:
                if first[j] > second[j]:
                    return -1
                if first[j] < second[j]:
                    return 1
        else:
            if type(first[j]) is int:
                out = compare([first[j]], second[j])
                if out == 1: 
                    return 1
                elif out == -1:
                    return -1
            if type(second[j]) is int:
                out = compare(first[j], [second[j]])
                if out == 1: 
                    return 1
                elif out == -1:
                    return -1
    return 0

packets = [ast.literal_eval(packet) for packet in data]
packets.sort(key=functools.cmp_to_key(compare))
packets.reverse()

print((packets.index(ast.literal_eval(p1))+1) * (packets.index(ast.literal_eval(p2))+1))