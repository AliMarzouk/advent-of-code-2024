from typing import List, Tuple
from copy import deepcopy

f = open("input.txt", "r")
input = f.read()

blocking_element = '#'

next_pos = {
    '^': (-1,0),
    '>': (0,1),
    '<': (0,-1),
    'v': (1,0),
}

next_dir = {
    '^': '>',
    '>': 'v',
    '<': '^',
    'v': '<',
}

def get_init_position(lines: List[str]) -> Tuple[int, int]:
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '^':
                return (i,j)
    raise Exception('Could not find the initial position of the guard.')

def isOutOfBounds(lines: List[str], line_pos: int, col_pos: int) -> bool:
    max_lines, max_columns = len(lines), len(lines[0])
    return line_pos < 0 or line_pos >= max_lines or col_pos < 0 or col_pos >= max_columns

def move_guard(lines: List[str], guard_dir: str, line_pos: int, col_pos: int) -> Tuple[str, int, int]:
    next_line_pos = line_pos + next_pos[guard_dir][0]
    next_col_pos = col_pos + next_pos[guard_dir][1]
    if not(isOutOfBounds(lines, next_line_pos, next_col_pos)) \
        and lines[next_line_pos][next_col_pos] == blocking_element:
        return (next_dir[guard_dir], line_pos, col_pos)
    return (guard_dir, next_line_pos, next_col_pos)

def partOne(input_str: str) -> int:
    lines = input_str.splitlines()
    max_lines, max_columns = len(lines), len(lines[0])
    guard_dir = '^'
    (guard_line_pos, guard_col_pos) = get_init_position(lines)
    visited_positions = set()
    while not(isOutOfBounds(lines, guard_line_pos, guard_col_pos)):
        visited_positions.add((guard_line_pos, guard_col_pos))
        (guard_dir, guard_line_pos, guard_col_pos) = move_guard(lines, guard_dir, guard_line_pos, guard_col_pos)

    return len(visited_positions)

def is_infinite_path(lines, guard_dir, guard_line_pos, guard_col_pos) -> bool:
    visited_positions = set() # set of (dir, line, col)
    while not(isOutOfBounds(lines, guard_line_pos, guard_col_pos)):
        if (guard_dir, guard_line_pos, guard_col_pos) in visited_positions:
            return True
        visited_positions.add((guard_dir, guard_line_pos, guard_col_pos))
        (guard_dir, guard_line_pos, guard_col_pos) = move_guard(lines, guard_dir, guard_line_pos, guard_col_pos)
    return False

def partTwo(input_str: str) -> int:
    lines = input_str.splitlines()
    max_lines, max_columns = len(lines), len(lines[0])
    guard_dir = '^'
    (guard_line_pos, guard_col_pos) = get_init_position(lines)
    obstucles_positions = {(guard_line_pos, guard_col_pos)}
    while not isOutOfBounds(lines, guard_line_pos, guard_col_pos):
        obstucle_line_pos, obstucle_col_pos = guard_line_pos + next_pos[guard_dir][0], guard_col_pos + next_pos[guard_dir][1]
        guard_dir_with_obstucle = next_dir[guard_dir] 
        if not isOutOfBounds(lines, obstucle_line_pos, obstucle_col_pos) \
            and not isOutOfBounds(lines, guard_line_pos, guard_col_pos):
            lines_with_obstucle = add_obstucle(lines, obstucle_line_pos, obstucle_col_pos)
            if is_infinite_path(lines_with_obstucle, guard_dir_with_obstucle, guard_line_pos, guard_col_pos):
                obstucles_positions.add((obstucle_line_pos, obstucle_col_pos))

        (guard_dir, guard_line_pos, guard_col_pos) = move_guard(lines, guard_dir, guard_line_pos, guard_col_pos)
    return len(obstucles_positions) - 1

def add_obstucle(lines, obstucle_line_pos, obstucle_col_pos):
    lines_with_obstucle = deepcopy(lines)
    lines_with_obstucle[obstucle_line_pos] = replace_char_index(lines_with_obstucle[obstucle_line_pos], obstucle_col_pos, '#')
    return lines_with_obstucle

def replace_char_index(string_replace, index, character):
    string_list = list(string_replace)
    string_list[index] = character
    return "".join(string_list)

# print(partOne(input)) #4580
# print(partTwo(input)) #1544 right answer


