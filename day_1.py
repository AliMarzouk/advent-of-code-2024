from typing import List, Tuple
import re

def calculateSimilarityPartTwo(input: str):
    (firstList, secondList) = getLists(input)
    occurrences = {}
    for element in secondList:
        occurrences[element] = occurrences.get(element, 0) + 1
    result = 0
    for element in firstList:
        result +=  element * occurrences.get(element, 0)
        
    return result
        

def calculateDistancePartOne(input: str) -> int:
    (firstList, secondList) = getLists(input)
    firstList.sort()
    secondList.sort()
    result = 0
    for (firstElement, secondElement) in zip(firstList, secondList):
        result += abs(firstElement - secondElement)
        
    return result


def getLists(puzzleInput: str) -> Tuple[List[int]]:
    firstList = []
    secondList = []
    for line in puzzleInput.splitlines():
        [firstElement, secondElement] = re.split(r'\s+', line)
        firstList.append(int(firstElement))
        secondList.append(int(secondElement))
        
    return (firstList, secondList)

def abs(value: int) -> int:
    return value if value > 0 else -value
    
f = open("input.txt", "r")
inputString = f.read()
print(calculateDistancePartOne(inputString))
print(calculateSimilarityPartTwo(inputString))
