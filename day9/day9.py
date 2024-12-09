from itertools import repeat

with open ('input.txt') as f:
    data = f.read()

def part1():
    result = 0

    emptyRange = []
    freeSpace = False
    disk = []
    id = -1
    freeSpots = 0

    for index, char in enumerate(data):
        if not freeSpace:
            id += 1
        else:
            freeSpots += int(char)
            if(int(char) > 0):
                emptyRange.append({ "start": len(disk), "length": int(char)})
        toAdd = str(id) if not freeSpace else '.'
        disk += int(char) * [toAdd]
        freeSpace = not freeSpace

    for range in emptyRange:
        length = range['length']
        index = range['start']

        while(length > 0 and freeSpots > 0):
            lastElement = disk.pop()
            if(lastElement == '.'):
                freeSpots -= 1
                continue
            length -= 1
            if (index < len(disk)):
                disk[index] = lastElement
            else:
                disk.append(lastElement)

            index += 1
            freeSpots -= 1
    
    for i, _ in enumerate(disk):
        result += i * int(disk[i])

    print(result)

def part2():
    result = 0

    emptyRange = []
    fileRange = []
    freeSpace = False
    disk = []
    id = -1
    freeSpots = 0

    for _, char in enumerate(data):
        if not freeSpace:
            id += 1
            fileRange.append({ "start": len(disk), "length": int(char), "id": int(id)})
        else:
            freeSpots += int(char)
            if(int(char) > 0):
                emptyRange.append({ "start": len(disk), "length": int(char)})
        toAdd = str(id) if not freeSpace else '.'
        disk += int(char) * [toAdd]
        freeSpace = not freeSpace

    for fRange in reversed(fileRange):
        for eRange in emptyRange:
            if (fRange['length'] <= eRange['length'] and eRange['start'] + eRange['length'] <= fRange['start']):
                length = fRange['length']
                eIndex = eRange['start']
                fIndex = fRange['start']
                while(length > 0):
                    disk[eIndex] = fRange['id']
                    disk[fIndex] = '.'
                    length -= 1
                    fIndex += 1
                    eIndex += 1

                eRange["length"] -= fRange['length']
                eRange["start"] += fRange['length']

                if (eRange["length"] == 0):
                    emptyRange.remove(eRange)
                break
                
    for i, _ in enumerate(disk):
        if(disk[i] != '.'):
            result += i * int(disk[i])

    print(result)


# part1()
part2()
