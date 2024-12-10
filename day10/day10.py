from itertools import repeat

with open ('input.txt') as f:
    data = [list(x) for x in f.read().splitlines()]

trailheads = []

for (row, line) in enumerate(data):
    for (col, char) in enumerate(line):
        if char == '0':
            trailheads.append((row, col))

def isInBounds(trailhead):
    (row, col) = trailhead
    return row >= 0 and row < len(data) and col >= 0 and col < len(data[0])

def getScore(trailhead, trailends, useRating):
    (row, col) = trailhead
    if data[row][col] == '9':
        if (not useRating):
            if (trailhead in trailends):
                return 0
        
        trailends.add(trailhead)
        return 1
    
    score = 0
    current = int(data[row][col])

    if (isInBounds((row + 1, col)) and data[row + 1][col] == str(current + 1)):
        score += getScore((row + 1, col), trailends, useRating)
    if (isInBounds((row, col + 1)) and data[row][col + 1] == str(current + 1)):
        score += getScore((row, col + 1), trailends, useRating)
    if (isInBounds((row - 1, col)) and data[row - 1][col] == str(current + 1)):
        score += getScore((row - 1, col), trailends, useRating)
    if (isInBounds((row, col - 1)) and data[row][col - 1] == str(current + 1)):
        score += getScore((row, col - 1), trailends, useRating)
    
    return score

def part1():
    result = 0

    for trailhead in trailheads:
        trailends = set()
        score = getScore(trailhead, trailends, False)
        result += score

    print(result)

def part2():
    result = 0

    for trailhead in trailheads:
        trailends = set()
        score = getScore(trailhead, trailends, True)
        result += score

    print(result)


part1()
part2()
