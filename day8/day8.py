from itertools import combinations

with open ('input.txt') as f:
    data = f.read().splitlines()
     
antennas = {}

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char != '.':
            antennas[char] = antennas.get(char, []) + [(i, j)]

def isInBounds(pair):
    (row, col) = pair
    return row >= 0 and col >= 0 and row < len(data[0]) and col < len(data)

def part1():
    antinodes = set()

    for _, nodes in antennas.items():
        for pair in combinations(nodes, 2):
            [(row1, col1), (row2, col2)] = pair
            rowDistance = abs(row1 - row2)
            colDistance = abs(col1 - col2)

            if (col1 > col2):
                #right top
                antinode1 = (min(row1, row2) - rowDistance, max(col1, col2) + colDistance)
                antinode2 = (max(row1, row2) + rowDistance, min(col1, col2) - colDistance)
            else:
                #left top
                antinode1 = (min(row1, row2) - rowDistance, min(col1, col2) - colDistance)
                antinode2 = (max(row1, row2) + rowDistance, max(col1, col2) + colDistance)
            
            if isInBounds(antinode1):
                antinodes.add(antinode1)

            if isInBounds(antinode2):
                antinodes.add(antinode2)
  
    print(len(antinodes))


def part2():
    antinodes = set()

    for _, nodes in antennas.items():
        for pair in combinations(nodes, 2):
            [(row1, col1), (row2, col2)] = pair
            rowDistance = abs(row1 - row2)
            colDistance = abs(col1 - col2)

            antinodes.add((row1, col1))
            antinodes.add((row2, col2))

            if (col1 > col2):
                #right top
                antinode1 = (min(row1, row2) - rowDistance, max(col1, col2) + colDistance)
                while(isInBounds(antinode1)):
                    antinodes.add(antinode1)
                    antinode1 = (antinode1[0] - rowDistance, antinode1[1] + colDistance)

                antinode2 = (max(row1, row2) + rowDistance, min(col1, col2) - colDistance)
                while(isInBounds(antinode2)):
                    antinodes.add(antinode2)
                    antinode2 = (antinode2[0] + rowDistance, antinode2[1] - colDistance)
            else:
                #left top
                antinode1 = (min(row1, row2) - rowDistance, min(col1, col2) - colDistance)
                while(isInBounds(antinode1)):
                    antinodes.add(antinode1)
                    antinode1 = (antinode1[0] - rowDistance, antinode1[1] - colDistance)
                antinode2 = (max(row1, row2) + rowDistance, max(col1, col2) + colDistance)
                while(isInBounds(antinode2)):
                    antinodes.add(antinode2)
                    antinode2 = (antinode2[0] + rowDistance, antinode2[1] + colDistance)

    print(len(antinodes))


part1()
part2()
