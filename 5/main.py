import itertools as it
import numpy as np
from functools import lru_cache

with open("5/input.txt") as f:
    lines = [line.rstrip() for line in f]
seed_numbers = np.array([int(s) for s in lines[1].strip().split(" ")])
ranges = []
for i in range(0, len(seed_numbers), 2):
    start = seed_numbers[i]
    length = seed_numbers[i + 1]
    ranges.append(range(start, start + length))

print("all ranges generated")

selection = lines[3:]

colons = [i for i, line in enumerate(selection) if ":" in line]
raw_maps = [
    selection[colons[i] + 1 : colons[i + 1] - 1] for i in range(len(colons) - 1)
]


def parse_map(m: list):
    roof = max([int(j) for line in m for j in line.split(" ")])
    print(f"roof is {roof}")
    source_to_target = []
    for line in m[::-1]:
        # src is index, dest is value
        dest, src, length = [int(j) for j in line.split(" ")]
        shift = dest - src
        print(f"Shift is {shift}")
        source_to_target.append({"span": range(src, src + length), "shift": shift})

    return source_to_target


def convert(inp: int, src_to_tgt: dict):
    for m in src_to_tgt:
        # print(inp, m["span"])
        if inp in m["span"]:
            return inp + m["shift"]
    return inp


def lowest_in_range(seed_range):
    low = 1000000000000
    for i, seed in enumerate(seed_range):
        if i % 100000 == 0:
            print(f"Progress = {round(100*(i/len(seed_range) / 10), 2)}%")
        res = seed_to_location(seed)
        if res < low:
            low = res
    return low


print(len(raw_maps))

maps = [parse_map(m) for m in raw_maps]
print("Maps parsed")


def seed_to_location(seed_num: int):
    # seed num first index, result is next index
    next_input = seed_num
    for m in maps:
        next_input = convert(next_input, m)
    return next_input


lowest = 100000000000
for i, srange in enumerate(ranges):
    print(
        f"starting range {i+1} out of {len(ranges)}, range is of length {len(srange)}"
    )
    low = lowest_in_range(srange)
    lowest = low if low < lowest else lowest
    print("minimum found")

print(f"lowest is: {lowest}")
