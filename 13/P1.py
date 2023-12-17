with open("13/input.txt") as f:
    raw_lines = [line.rstrip() for line in f]
import numpy as np

groups = []
blanks = [i for i in range(len(raw_lines)) if not raw_lines[i]]
prev = -1
for b in blanks:
    groups.append(raw_lines[prev + 1 : b])
    prev = b
groups.append(raw_lines[prev + 1 :])


def match_group(group: list):
    match_index = -1
    for i, line in enumerate(group):
        j = i  # to iterate again
        prev_index = i - 1
        prev = group[prev_index] if i > 0 else []
        while line == prev:
            # print(f"Match found! {line} equals {line}")
            match_index = i
            prev_index -= 1
            j += 1
            if prev_index < 0:
                return match_index
            try:
                line = group[j]
                prev = group[prev_index]
            except IndexError:
                return match_index
    return -1


def score_from_group(group):
    tot = 0
    hori_pos = match_group(group)
    rot_arr = np.rot90(np.array([list(l) for l in group]), -1)
    rot = list([list(subarr) for subarr in rot_arr])
    # print(f"sending in {rot}")
    vert_pos = match_group(rot)
    hori_score = 100 * hori_pos if hori_pos >= 0 else 0
    vert_score = vert_pos if vert_pos >= 0 else 0
    tot += hori_score
    tot += vert_score
    if tot == 0:
        print(f"No match on {group}")
    return tot


total = 0

for group in groups:
    total += score_from_group(group)
    # print(f"adding {score_from_group(group)}")

print(total)
# add up the number of columns to the left of each vertical line of reflection;
# 25357 - answer is too low
# 32704 - answer is too low
