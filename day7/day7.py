from itertools import cycle, dropwhile

with open ('input.txt') as f:
    data = f.read().splitlines()

def canSolve(target, current, numbers, concat):
    if(target == current and len(numbers) == 0):
        return True
    
    if len(numbers) == 0:
        return False
    
    nextNum = numbers.pop(0)
    sum = canSolve(target, current + nextNum, numbers.copy(), concat)
    mult = canSolve(target, current * nextNum, numbers.copy(), concat)

    if (concat):
        concat = canSolve(target, int(str(current) + str(nextNum)), numbers.copy(), concat)
        return sum or mult or concat
    else:
        return sum or mult
    
def part1():
    result = 0
    
    for line in data:
        target, numbers = line.split(': ')
        numbers = [int(x) for x in numbers.split(' ')]
        target = int(target)
        if canSolve(target, 0, numbers.copy(), False):
            result += target
    
    print(result)


def part2():
    result = 0
    
    for line in data:
        target, numbers = line.split(': ')
        numbers = [int(x) for x in numbers.split(' ')]
        target = int(target)
        if canSolve(target, 0, numbers.copy(), True):
            result += target
    
    print(result)


part1()
part2()
