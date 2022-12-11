
import numpy as np
import operator

with open('day11\input.txt', 'r') as file:
    data = [monkey.split("\n") for monkey in file.read().split("\n\n")]

# print(data)

class Monkey:
    def __init__(self, id, items, testVal, testTrue, testFalse, operation) -> None:
        self.id = id
        self.items = items
        self.testVal = testVal
        self.testTrue = testTrue
        self.testFalse = testFalse
        self.operation = operation
        self.counter = 0
    
    def test(self, number):
        if number % self.testVal == 0:
            return self.testTrue
        else:
            return self.testFalse
    
    def addItem(self, level):
        self.items.append(level)

ops = {"+": operator.add, "*": operator.mul}

all_monkeys = []
for monkey in data:
    id = monkey[0].split(" ")[1][:-1]
    items = [int(val) for val in monkey[1].replace("  Starting items: ","").replace(",","").split(" ")]
    op = monkey[2].replace("  Operation: new = old ","").split(" ")
    testVal = int(monkey[3].replace("  Test: divisible by ",""))
    testTrue = int(monkey[4].replace("    If true: throw to monkey ",""))
    testFalse = int(monkey[5].replace("    If false: throw to monkey ",""))
    all_monkeys.append(Monkey(id, items, testVal, testTrue, testFalse, op))

for _ in range(20):
    for monkey in all_monkeys:
        for item in monkey.items:
            op = monkey.operation
            if op[1] == 'old':
                new_level = ops[op[0]](item,item)
            else:
                new_level = ops[op[0]](item,int(op[1]))
            new_level //= 3
            sendTo = monkey.test(new_level)
            all_monkeys[sendTo].addItem(new_level)
            monkey.counter += 1
        monkey.items = []

all_counters = []
for monkey in all_monkeys:
    # print(f'Monkey {monkey.id}: {monkey.items} and counter: {monkey.counter}')
    all_counters.append(monkey.counter)

print(np.prod(sorted(all_counters, reverse=True)[:2]))