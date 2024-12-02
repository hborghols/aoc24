with open ('input.txt') as f:
    data = f.read().splitlines()
    
def isLineSafe(line):
    splitLine = (line.split(' '))
    increasing = True
    safe = False
    for i in range(1, len(splitLine)):
        if (i == 1):
            if (int(splitLine[i]) > int(splitLine[i-1])):
                increasing = True
            else:
                increasing = False
        
        diff = int(splitLine[i]) - int(splitLine[i - 1])
        if (increasing == True and diff > 0 and diff <= 3):
            safe = True
        elif (increasing == False and diff < 0 and diff >= -3):
            safe = True
        else:
            safe = False
            break
        
    return safe
            
def isDampenedLineSafe(line):
    splitLine = (line.split(' '))  
    isSafePossible = False
    for level in range(len(splitLine)):
        lineCopy = splitLine.copy()
        del lineCopy[level]
        if (isLineSafe(' '.join(lineCopy))):
            isSafePossible = True
            break
        
    return isSafePossible

def part1():
    result = 0

    for line in data:
        if isLineSafe(line):
            result += 1

    print(result)

def part2():
    result = 0
    
    for line in data:
        if isDampenedLineSafe(line):
            result += 1

    print(result)

part1()
part2()