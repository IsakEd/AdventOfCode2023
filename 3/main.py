import numpy as np
from itertools import product

with open("3/input.txt") as f:
    lines = [line.rstrip() for line in f]

mat = np.array([list(line) for line in lines])


def number_from_start_position(start_pos: int, line: str):
    sequence = ""
    for i in range(start_pos, len(line)):
        if i == len(line) - 1:
            if line[i].isnumeric():
                sequence += line[i]
                return int(sequence)
            else:
                return int(sequence)
        if not line[i].isnumeric():
            return int(sequence)
        sequence += line[i]


def numbers_in_line(line_index: int):
    line = lines[line_index]
    number_start_positions = []
    for i, n in enumerate(line):
        if (n.isnumeric() and i == 0) or (
            n.isnumeric() and not line[i - 1].isnumeric()
        ):
            number_start_positions.append(i)
    numbers = [number_from_start_position(pos, line) for pos in number_start_positions]
    if numbers:
        return {
            num: start_pos
            for num, start_pos in zip(
                numbers, [(line_index, c) for c in number_start_positions]
            )
        }
    else:
        return []


def is_symbol(char: str):
    return char != "." and (not char.isnumeric())


def get_adjacent_positions(row_idx: int, col_start_idx: int, length: int):
    col_span = set(range(col_start_idx - 1, col_start_idx + length + 1)).intersection(
        set(range(len(lines[0])))
    )
    row_span = set(range(row_idx - 1, row_idx + 2)).intersection(
        set(range(len(lines[0])))
    )
    positions = list(set([(r, c) for r, c in product(row_span, col_span)]))
    return positions


def get_part_numbers(line_index, mat):
    pnums_in_line = []
    numbers = numbers_in_line(line_index)  # All good
    for number in numbers:
        start_pos = numbers[number]  # All good
        adj_pos = get_adjacent_positions(start_pos[0], start_pos[1], len(str(number)))
        if any([is_symbol(mat[p[0]][p[1]]) for p in adj_pos]):
            pnums_in_line.append(number)
    return pnums_in_line


total = 0
for i, line in enumerate(lines):
    pnums = get_part_numbers(i, mat)
    total += pnums
    print(pnums)
print(total)
