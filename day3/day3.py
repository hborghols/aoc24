import re

with open ('input.txt') as f:
    data = f.read()
    
def part1():
    result = 0

    instructions = re.compile(r"mul\(\d+,\d+\)").findall(data)

    for instruction in instructions:
        numbers = re.compile(r"\d+").findall(instruction)
        result += int(numbers[0]) * int(numbers[1])

    print(result)

def part2():
    result = 0

    instructions = re.compile(r"don't|do|mul\(\d+,\d+\)").findall(data)
    processInstruction = True

    for instruction in instructions:
        if(instruction == "don't"):
            processInstruction = False
            continue
        elif(instruction == "do"):
            processInstruction = True
            continue

        if(processInstruction):
            numbers = re.compile(r"\d+").findall(instruction)
            result += int(numbers[0]) * int(numbers[1])

    print(result)

part1()
part2()