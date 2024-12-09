f = open("input.txt", "r")
input = f.read()
TEST_WORD = 'XMAS'

def partOne(input_str: str) -> int:
    max_lines, max_columns = len(input_str.splitlines()) , len(input_str.splitlines()[0])
    lines = input_str.splitlines()
    result = 0
    variations = [(-1,-1),(1,1),(-1,1),(1,-1),(1,0),(-1,0),(0,1),(0,-1)]

    def evaluate(count, line_index, col_index, variation):
        if line_index >= max_lines or col_index >= max_columns or line_index < 0 or col_index < 0 or lines[line_index][col_index] != TEST_WORD[count]:
            return 0
        if count == 3:
            return 1
        return evaluate(count + 1, line_index + variation[0], col_index + variation[1], variation)

    for i in range(max_lines):
        for j in range(max_columns):
            if lines[i][j] == 'X':
                for variation in variations:
                    result += evaluate(0, i, j, variation)

    return result

def partTwo(input_str: str) -> int:
    max_lines, max_columns = len(input_str.splitlines()) , len(input_str.splitlines()[0])
    lines = input_str.splitlines()
    result = 0

    def evaluate(line_index, col_index):
        if line_index + 1 >= max_lines or col_index + 1 >= max_columns or line_index - 1 < 0 or col_index - 1 < 0:
            return 0
        if set([(lines[line_index-1][col_index-1], lines[line_index-1][col_index+1]),(lines[line_index+1][col_index-1], lines[line_index+1][col_index+1])]) == set([('M','M'),('S','S')]) \
        or set([(lines[line_index-1][col_index-1], lines[line_index+1][col_index-1]),(lines[line_index-1][col_index+1], lines[line_index+1][col_index+1])]) == set([('M','M'),('S','S')]):
            return 1
        return 0

    for i in range(max_lines):
        for j in range(max_columns):
            if lines[i][j] == 'A':
                result += evaluate(i, j)

    return result

print(partOne(input)) #2547
print(partTwo(input)) #1939