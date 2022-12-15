import ast

with open('day13\input.txt', 'r') as file:
    data = [pair.split("\n") for pair in file.read().split("\n\n")]
# print(data)

def compare(pair):
    first = pair[0]
    second = pair[1]
    l = max(len(first),len(second))
    for j in range(l):
        if len(first)!=len(second):
            try:
                dummy = second[j]
            except IndexError:
                return False
            try:
                dummy = first[j]
            except IndexError:
                return True
        if type(first[j]) == type(second[j]):
            if type(first[j]) is list:
                out = compare([first[j], second[j]])
                if out == True: 
                    return True
                elif out == False:
                    return False
            if type(first[j]) is int:
                if first[j] > second[j]:
                    return False
                if first[j] < second[j]:
                    return True
        else:
            if type(first[j]) is int:
                out = compare([[first[j]], second[j]])
                if out == True: 
                    return True
                elif out == False:
                    return False
            if type(second[j]) is int:
                out = compare([first[j], [second[j]]])
                if out == True: 
                    return True
                elif out == False:
                    return False


result = 0
for i, pair in enumerate(data):
    packets = [ast.literal_eval(packet) for packet in pair]    
    out = compare(packets)
    if out:
        result += i+1
print(result)