with open ('input.txt') as f:
    data = f.read().splitlines()

listOne = []
listTwo = []

for line in data:
    splitLine = (line.split('   '))
    listOne.append(splitLine[0])
    listTwo.append(splitLine[1])
    
def part1():
    sortedOne = sorted(listOne)
    sortedTwo = sorted(listTwo)
    distance = 0

    for i in range(len(listOne)):
        distance += abs(int(sortedTwo[i]) - int(sortedOne[i]))

    print(distance)

def part2():
    appearances = {}
    similarity = 0

    for i in range(len(listTwo)):
        appearances[listTwo[i]] = appearances.get(listTwo[i], 0) + 1

    for i in range(len(listOne)):
        similarity += int(listOne[i]) * appearances.get(listOne[i], 0)
    
    print(similarity)

part1()
part2()