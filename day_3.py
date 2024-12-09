f = open("input.txt", "r")
input = f.read()

import re

def getMuliplicationResultPartOne(inputString: str) -> int:
    return sum(map(lambda x: x[0]*x[1], map(lambda x: eval(x), re.findall(r"mul\((\d+,\d+)\)", inputString))))

def getMuliplicationResultPartTwo(inputString: str) -> int:
    """
    NOT WORKING
    """
    potential_found_list = re.findall(r".*?mul\(\d+,\d+\)", inputString)
    print(len(potential_found_list))
    print(potential_found_list)
    def checkActivated(element: str) -> bool:
        print('dont', re.search(r"don't\(\)(?!.*don't\(\))", element))
        print('do', re.search(r"do\(\)(?!.*do\(\))", element))
        if deactivatedMatch := re.search(r"don't\(\)(?!.*don't\(\))", element):
            print('deactivated', deactivatedMatch)
            if activatedMatch := re.search(r"do\(\)(?!.*do\(\))", element):
                return activatedMatch > deactivatedMatch
        return True

    test_fn = lambda potential: eval(re.search(r"mul\((\d+,\d+)\)", potential).group(1))
    return sum(map(lambda x: x[0]*x[1], map(test_fn, filter(checkActivated, potential_found_list))))

print(getMuliplicationResultPartOne(input)) #174103751

# print(getMuliplicationResultPartTwo("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")) #wrong 10959092 answer too low 
# print(re.search(r"(?:do())?.*?mul\(\d+,\d+\)", ""))