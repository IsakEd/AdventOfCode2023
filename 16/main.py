import sys

with open("16/input.txt") as f:
    grid = [line.rstrip() for line in f]


def next_position(pos: tuple, instruction: str) -> tuple:
    row, col = pos
    match instruction:
        case "U":
            return (row - 1, col)
        case "D":
            return (row + 1, col)
        case "L":
            return (row, col - 1)
        case "R":
            return (row, col + 1)


def get_instruction(symbol: str, last_dir: str):
    slash_dirs = "RURDLD"
    backslash_dirs = "RDRLUL"

    match symbol:
        case ".":
            return last_dir
        case "|":
            return ["U", "D"] if last_dir == "L" or last_dir == "R" else last_dir
        case "-":
            return ["L", "R"] if last_dir == "U" or last_dir == "D" else last_dir
        case "/":
            return slash_dirs[slash_dirs.find(last_dir) + 1]
        case "\\":
            return backslash_dirs[backslash_dirs.find(last_dir) + 1]


def is_inside(pos: tuple, grid: list) -> bool:
    row, col = pos
    in_row_span = row >= 0 and row < len(grid)
    in_column_span = col >= 0 and col < len(grid[0])
    return in_row_span and in_column_span


def traverse(grid, pos, direction, state):
    stack, seen, light = [state["stack"], state["seen"], state["light"]]
    stack.pop(-1)
    seen.add((pos, direction))
    light.add(pos)
    sym = grid[pos[0]][pos[1]]
    next_position
    instructions = get_instruction(sym, direction)
    for ins in instructions:
        next_pos = next_position(pos, ins)
        if is_inside(next_pos, grid) and (next_pos, ins) not in seen:
            stack.append((next_pos, ins))
    return


def count_energized(start_pos, start_direction, grid):
    state = {"light": set(), "seen": set(), "stack": [(start_pos, start_direction)]}

    while len(state["stack"]) > 0:
        position, direction = state["stack"][-1]
        traverse(grid, position, direction, state)
    return len(state["light"])


p1_start = ((0, 0), "R")
p1_ans = count_energized(*p1_start, grid)
print(p1_ans)

# P2
p2_starts = []  # (pos_tuple, dir_string)
for i in range(len(grid)):
    p2_starts.append(((i, 0), "R"))
    p2_starts.append(((i, len(grid[0]) - 1), "L"))
for i in range(len(grid[0])):
    p2_starts.append(((0, i), "D"))
    p2_starts.append(((len(grid) - 1, i), "U"))

print(max([count_energized(*init, grid) for init in p2_starts]))
