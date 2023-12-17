import numpy as np

with open("13/input.txt") as f:
    raw_lines = [line.rstrip() for line in f]


groups = []
blanks = [i for i in range(len(raw_lines)) if not raw_lines[i]]
prev = -1
for b in blanks:
    groups.append(raw_lines[prev + 1 : b])
    prev = b
groups.append(raw_lines[prev + 1 :])


class Cleaner:
    times_cleaned = 0
    just_cleaned = False

    def needs_fix(self, line1, line2):
        count = 0
        for ch1, ch2 in zip(line1, line2):
            count += int(ch1 != ch2)
        fix = count == 1
        if fix:
            self.times_cleaned += 1

        self.just_cleaned = fix if self.times_cleaned == 1 else False
        return fix if self.times_cleaned == 1 else False


class PartTwoSolver:
    group = []
    cleaner = {}

    def __init__(self, mat) -> None:
        self.cleaner = Cleaner()
        self.group = mat
        print(f"It is now the start, the group is")
        print(self.group)

    def rotate_group(self):
        rot_arr = np.rot90(np.array([list(l) for l in self.group]), -1)
        self.group = list([list(subarr) for subarr in rot_arr])

    def match_group(self):
        cleaner = self.cleaner
        match_index = -1
        for i, line in enumerate(self.group):
            j = i  # to iterate again
            prev_index = i - 1
            prev = self.group[prev_index] if i > 0 else []
            while line == prev or cleaner.needs_fix(line, prev):
                match_index = i
                prev_index -= 1
                if cleaner.just_cleaned:
                    print(f"cleaned at line {i}")
                    line = prev
                    print(self.group[prev_index], self.group[j])
                    self.group[j] = self.group[prev_index + 1]
                    print("The group is now")
                    print(self.group)
                j += 1
                if prev_index < 0:
                    return match_index
                try:
                    line = self.group[j]
                    prev = self.group[prev_index]
                except IndexError:
                    return match_index
        return -1

    def score_from_group(self, group):
        tot = 0
        hori_pos = self.match_group()
        self.rotate_group()
        vert_pos = -1 if hori_pos >= 0 else self.match_group()
        hori_score = 100 * hori_pos if hori_pos >= 0 else 0
        vert_score = vert_pos if vert_pos >= 0 else 0
        tot += hori_score
        tot += vert_score
        if vert_score and hori_score:
            print(vert_score, hori_score)
            print("This shouldn't happen!")
        if tot == 0:
            print(f"No match on {group}")
        return tot


total = 0

for group in groups:
    sol = PartTwoSolver(group)
    total += sol.score_from_group(group)
    # print(f"adding {score_from_group(group)}")

print(total)
# add up the number of columns to the left of each vertical line of reflection;
# 25357 - answer is too low
# 32704 - answer is too low

# P2
# 36916 is too high
# 36830 is too high
# 31223 is not right
# 31804 is not right

p = groups[0]
p = [[3, 5, 1, 3]]
print([*(*p)])
