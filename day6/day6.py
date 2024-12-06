from itertools import cycle, dropwhile

with open ('input.txt') as f:
    data = [list(x) for x in f.read().splitlines()]

yBound = len(data)
xBound = len(data[0])

startX, startY = -1, -1

for lineIndex, line in enumerate(data):
    if ('^' in line):
        startX = line.index('^')
        startY = lineIndex

directions = {
    'up': {'y': -1, 'x': 0},
    'right': {'y': 0, 'x': 1},
    'down': {'y': 1, 'x': 0},
    'left': {'y': 0, 'x': -1},
}

def part1():
    result = 0
    directionsCycle = cycle(directions)
    direction = next(directionsCycle)
    x, y = startX, startY
    seen = set()

    while True:
        new = (x, y)
        if new not in seen:
            result += 1
            seen.add(new)

        newY = y + directions[direction]['y']
        newX = x + directions[direction]['x']

        if (newY < 0 or newY >= yBound or newX < 0 or newX >= xBound):
            break
       
        nextStep = data[newY][newX]
        if(nextStep == '#'):
            direction = next(directionsCycle)
            
        x = x + directions[direction]['x']
        y = y + directions[direction]['y']

    print(result)

def isLoop():
    y, x = startY, startX
    directionsCycle = cycle(directions)
    direction = next(directionsCycle)
    seen = set()

    while True:         
        if (x, y, direction) in seen:
            return True
        seen.add((x, y, direction))

        newY = y + directions[direction]['y']
        newX = x + directions[direction]['x']

        if (newY < 0 or newY >= yBound or newX < 0 or newX >= xBound):
            break
       
        if(data[newY][newX] == '#'):
            direction = next(directionsCycle)
        else:
            x += directions[direction]['x']
            y += directions[direction]['y']
        
    return False

def part2():
    result = 0
    directionsCycle = cycle(directions)
    direction = next(directionsCycle)
    y, x = startY, startX

    while (y > 0 and y < yBound and x > 0 and x < xBound):
        newY = y + directions[direction]['y']
        newX = x + directions[direction]['x']

        if (newY < 0 or newY >= yBound or newX < 0 or newX >= xBound):
            break
       
        nextStep = data[newY][newX]
        while(nextStep == '#'):
            direction = next(directionsCycle)
            newY = y + directions[direction]['y']
            newX = x + directions[direction]['x']
            nextStep = data[newY][newX]
        
        if (data[newY][newX] == '.'):
            temp = data[newY][newX]
            data[newY][newX] = '#'
            if (isLoop()):
                result += 1
                data[newY][newX] = '*'
            else:
                data[newY][newX] = temp
            
        x = newX
        y = newY

    print(result)


part1()
part2()
