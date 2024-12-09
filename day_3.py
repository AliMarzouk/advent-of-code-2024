f = open("input.txt", "r")
input = f.read()

import re

def getMuliplicationResultPartOne(inputString: str) -> int:
    return sum(map(lambda x: x[0]*x[1], map(lambda x: eval(x), re.findall(r"mul\((\d+,\d+)\)", inputString))))

def getMuliplicationResultPartTwo(inputString: str, active: bool = True) -> int:
    do_match = re.search("do()", inputString)
    do_position = do_match.start() if do_match else None
    dont_match = re.search("don't()", inputString)
    dont_position = dont_match.start() if dont_match else None
    matches = re.finditer(r"mul\((\d+,\d+)\)", inputString, re.MULTILINE)
    result = 0
    for match in matches:
        if dont_position != None and dont_position < match.start():
            return result + getMuliplicationResultPartTwo(inputString[dont_position+5:], False)
        if active or (do_position != None and match.start() > do_position):
            numbers = eval(match.group(1))
            result = result + (int(numbers[0]) * int(numbers[1]))

    return result
        

print(getMuliplicationResultPartOne(input)) #174103751
print(getMuliplicationResultPartTwo(input)) #100411201