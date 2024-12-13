with open ('input.txt') as f:
    data = [int(x) for x in f.read().split(' ')]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

splitMap = {}
multMap = {}

def blinkList(stones):
    current = stones.head
    length = 0
    while current:
        length += 1
        if (current.value == 0):
            current.value = 1
        elif (len(str(current.value)) % 2 == 0):
            if (splitMap.get(current.value)):
                firstpart, secondpart = splitMap[current.value]
            else:
                string = str(current.value)
                firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                firstpart, secondpart = int(firstpart), int(secondpart)
            current.value = firstpart
            newNode = Node(secondpart)
            newNode.next = current.next
            current.next = newNode
            current = newNode
            length += 1
        else:
            if (multMap.get(current.value)):
                current.value = multMap[current.value]
            else:
                newValue = current.value * 2024
                multMap[current.value] = newValue
                current.value = newValue

        current = current.next   

    return length

def blinkRecursive(stone, blinks, memo):
    if (blinks == 0):
        return 1
    
    key = str(stone) + '-' + str(blinks)

    if (memo.get(key)):
        return memo[key]
    
    blinks -= 1

    if (stone == 0):
        numberOfStones = blinkRecursive(1, blinks, memo)
    elif (isEven(stone)):
        if (splitMap.get(stone)):
            firstpart, secondpart = splitMap[stone]
        else:
            string = str(stone)
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
            firstpart, secondpart = int(firstpart), int(secondpart)
            splitMap[stone] = (firstpart, secondpart)
        
        numberOfStones = blinkRecursive(firstpart, blinks, memo) + blinkRecursive(secondpart, blinks, memo)
    else:
        if(multMap.get(stone)):
            new = multMap[stone]
        else:
            new = stone * 2024
            multMap[stone] = new
        
        numberOfStones = blinkRecursive(new, blinks, memo)
    
    memo[key] = numberOfStones

    return numberOfStones

def part1():
    print('Part 1')
    firstStone = Node(data[0])
    stones = LinkedList(firstStone)

    result = 0
    for i in range(1, len(data)):
        stones.append(data[i])
   
    for i in range(25):
        result =  blinkList(stones)

    print(result)

def isEven(n):
    return len(str(n)) % 2 == 0

def part22slow():
    print('Part 2')
    zeroes = []
    even = []
    other = []

    stones = data.copy()
    for i in range(len(stones)):
        if (stones[i] == 0):
            zeroes += [stones[i]]
        elif (len(str(stones[i])) % 2 == 0):
            even += [stones[i]]
        else:
            other += [stones[i]]

    for i in range(75):
        newZeroes = []
        newEven = []
        newOther = []
        for j in range(max(len(zeroes), len(even), len(other))):
            if (j in range(len(zeroes))):
                newOther += [1]
            if (j in range(len(even))):
                if (splitMap.get(even[j])):
                    firstpart, secondpart = splitMap[even[j]]
                else:
                    string = str(even[j])
                    firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                    firstpart, secondpart = int(firstpart), int(secondpart)
                    splitMap[even[j]] = (firstpart, secondpart)
                
                for part in (firstpart, secondpart):
                    if (isEven(part)):
                        newEven += [part]
                    elif (part == 0):
                        newZeroes += [part]
                    else:
                        newOther += [part]
            if (j in range(len(other))):
                if(multMap.get(other[j])):
                    new = multMap[other[j]]
                else:
                    new = other[j] * 2024
                    multMap[other[j]] = new
                
                if (isEven(new)):
                    newEven += [new]
                elif (new == 0):
                    newZeroes += [new]
                else:
                    newOther += [new]
            
        zeroes = newZeroes
        even = newEven
        other = newOther

    print(len(zeroes) + len(even) + len(other))

def part2():
    print('Part 2')
    stones = data.copy()

    result = 0
    for i in range(len(stones)):
        result += blinkRecursive(stones[i], 75, {})

    print(result)

part1()
part2()
