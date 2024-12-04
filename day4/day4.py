with open ('input.txt') as f:
    data = f.read().splitlines()
    
def part1():
    result = 0

    for lineIndex, line in enumerate(data):
        for charIndex, char in enumerate(line):
            #start of word
            if(char == 'X'):
                #forward word
                if (charIndex < len(line) - 3 and line[charIndex + 1] == 'M' and line[charIndex + 2] == 'A' and line[charIndex + 3] == 'S'):
                    result += 1
                #backward word
                if (charIndex > 2 and line[charIndex - 1] == 'M' and line[charIndex - 2] == 'A' and line[charIndex - 3] == 'S'):
                    result += 1
                #upward word
                if (lineIndex > 2 and data[lineIndex - 1][charIndex] == 'M' and data[lineIndex - 2][charIndex] == 'A' and data[lineIndex - 3][charIndex] == 'S'):
                    result += 1
                #diagonal right up word
                if (lineIndex > 2 and charIndex < len(line) - 3 and data[lineIndex - 1][charIndex + 1] == 'M' and data[lineIndex - 2][charIndex + 2] == 'A' and data[lineIndex - 3][charIndex + 3] == 'S'):
                    result += 1
                #diagonal left up word
                if (lineIndex > 2 and charIndex > 2 and data[lineIndex - 1][charIndex - 1] == 'M' and data[lineIndex - 2][charIndex - 2] == 'A' and data[lineIndex - 3][charIndex - 3] == 'S'):
                    result += 1
                #downward word
                if (lineIndex < len(data) - 3 and data[lineIndex + 1][charIndex] == 'M' and data[lineIndex + 2][charIndex] == 'A' and data[lineIndex + 3][charIndex] == 'S'):
                    result += 1
                #diagonal right down word
                if (lineIndex < len(data) - 3 and charIndex < len(line) - 3 and data[lineIndex + 1][charIndex + 1] == 'M' and data[lineIndex + 2][charIndex + 2] == 'A' and data[lineIndex + 3][charIndex + 3] == 'S'):
                    result += 1
                #diagonal left down word
                if (lineIndex < len(data) - 3 and charIndex > 2 and data[lineIndex + 1][charIndex - 1] == 'M' and data[lineIndex + 2][charIndex - 2] == 'A' and data[lineIndex + 3][charIndex - 3] == 'S'):
                    result += 1

    print(result)

def part2():
    result = 0

    for lineIndex, line in enumerate(data):
        for charIndex, char in enumerate(line):
            # middle of X-MAS
            if (char == 'A' and lineIndex > 0 and lineIndex < len(data) - 1 and charIndex > 0 and charIndex < len(line) - 1):
                TL = data[lineIndex - 1][charIndex - 1]
                TR = data[lineIndex - 1][charIndex + 1]
                BL = data[lineIndex + 1][charIndex - 1]
                BR = data[lineIndex + 1][charIndex + 1]
                
                if (TL == 'M' and TR == 'M' and BL == 'S' and BR == 'S'):
                    result += 1
                elif (TL == 'M' and TR == 'S' and BL == 'M' and BR == 'S'):
                    result += 1
                elif (TL == 'S' and TR == 'S' and BL == 'M' and BR == 'M'):
                    result += 1
                elif (TL == 'S' and TR == 'M' and BL == 'S' and BR == 'M'):
                    result += 1

    print(result)

part1()
part2()