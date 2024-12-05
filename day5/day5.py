import math

with open ('input.txt') as f:
    data = f.read()
    
rules, updates = data.split("\n\n")
rules = rules.split("\n")
updates = updates.split("\n")
shouldComeAfter = {}
shouldComeBefore = {}

for rule in rules:
    rule = rule.split("|")
    shouldComeAfter[rule[0]] = shouldComeAfter.get(rule[0], []) + [rule[1]]

correctUpdates = []
incorrectUpdates = []

for update in updates:
    pages = update.split(",")
    seenPages = []
    correct = True

    for page in pages:
        for rule in shouldComeAfter.get(page, []):
            if rule in seenPages:
                correct = False
                break
        seenPages.append(page)
                
    if correct:
        correctUpdates.append(pages)
    else:
        incorrectUpdates.append(pages)

def part1():
    result = sum([int(x[math.floor(len(x) / 2)]) for x in correctUpdates])

    print(result)

def part2():
    correctedUpdates = []

    for pages in incorrectUpdates:
        corrected = []
        for page in pages:
            newIndex = len(corrected)
            found = False
            for rule in shouldComeAfter.get(page, []):
                if rule in corrected:
                    #if there is a page that should come after the current page and it is already in the list, then the current page should come before that page
                    newIndex = min(corrected.index(rule), newIndex)
                    found = True
                    
            if found:
                corrected.insert(newIndex, page)
            else:
                corrected.append(page)

        correctedUpdates.append(corrected)        

    result = sum([int(x[math.floor(len(x) / 2)]) for x in correctedUpdates])

    print(result)

part1()
part2()