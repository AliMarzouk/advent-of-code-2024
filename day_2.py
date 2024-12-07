from typing import List

def calculateSafetyPartOne(puzzleInput: str) -> int:
    reports = getReports(puzzleInput)
    result = 0
    for report in reports:
        result += int(checkReport(report))
        
    return result

def calculateSafetyPartTwo(puzzleInput: str) -> int:
    reports = getReports(puzzleInput)
    result = 0
    for report in reports:
        result += int(checkReportWithTolerance(report))
        
    return result

def getReports(puzzleInput: str) -> List[List[int]]:
    reports = []
    for line in puzzleInput.splitlines():
        reports.append(list(map(int, line.split(' '))))
        
    return reports

def abs(value: int) -> int:
    return value if value > 0 else -value

def checkReport(report: List[int]) -> bool:
    def partialCheck(report: List[int], increasing: bool) -> bool:
        if not report or len(report) == 1:
            return True
        if not(isSafe(report[0], report[1], increasing)):
            return False
        else:
            return partialCheck(report[1:], increasing)
            
    return partialCheck(report, report [0] < report[1])

def isSafe(firstLevel: int, secondLevel: int, increasing: bool) -> bool:
    return (firstLevel < secondLevel) == increasing and abs(firstLevel - secondLevel) <= 3 and firstLevel != secondLevel

def isSafePartTwo(firstLevel: int, secondLevel: int, thirdLevel: int, forthLevel: int = None) -> bool:
    return abs(secondLevel - thirdLevel) <= 3 \
        and secondLevel != thirdLevel \
            and (firstLevel == None or ((firstLevel < secondLevel) == (secondLevel < thirdLevel))) \
            and (forthLevel == None or ((secondLevel < thirdLevel) == (thirdLevel < forthLevel))) \

def checkReportWithTolerance(report: List[int]) -> bool:
    """
    The function verifies recursively if a given list of integer is safe according to the rules of part2.
    The principle of the verification is to consider that at any given position that the past seen list valid and try to remove one element 
    and check the rest of the list without that element. 

    Args:
        report (List[int]): list of integers to check

    Returns:
        bool: true if the list is valid by removing maximum one element, false otherwise.
    """
    def partialCheckWithTolerance(report: List[int], tolerate: bool, previousElement: int) -> bool:
        if not report or len(report) == 1:
            return True
        if len(report) == 2:
            if isSafePartTwo(previousElement, report[0], report[1]):
                return True
            elif tolerate:
                return partialCheckWithTolerance(report[1:], False, report[0])
            else:
                return False
        if isSafePartTwo(previousElement, report[0], report[1], report[2]):
            return partialCheckWithTolerance(report[1:], tolerate, report[0])
        if tolerate:
            withoutFirst = report[:]
            del withoutFirst[1]
            withoutSecond = report[:]
            del withoutSecond[2]
            return partialCheckWithTolerance(withoutFirst, False, previousElement) or partialCheckWithTolerance(withoutSecond, False, previousElement)
        else:
            return False
    
    if isSafePartTwo(None, report[0], report[1], report[2]):
        return partialCheckWithTolerance(report, True, None)
    else:
        return partialCheckWithTolerance(report[1:], False, None) or partialCheckWithTolerance(report, True, None)


f = open("input.txt", "r")
inputString = f.read()
print(calculateSafetyPartOne(inputString)) # should be 359
print(calculateSafetyPartTwo(inputString)) # should be 418
