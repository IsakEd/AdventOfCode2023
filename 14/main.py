with open("14/input.txt") as f:
    lines = [line.rstrip() for line in f]


def rotate(lines):
    return ["".join(t)[::-1] for t in [*zip(*lines)]]


def slide(line):
    def slide_seg(seg: str):
        n = sum([(c == "O") for c in seg])
        return "." * (len(seg) - n) + "O" * n

    segments = [[slide_seg(seg) for seg in line.split("#")]]
    new_line = "#".join(*segments)
    return new_line


def score_line(line):
    return sum(i + 1 for i, ch in enumerate(line) if ch == "O")


p1 = sum(map(score_line, map(slide, rotate(lines))))


def cycle(lines):
    tmp_lines = lines
    for _ in range(4):
        tmp_lines = rotate(tmp_lines)
        tmp_lines = [slide(line) for line in tmp_lines]
    return tmp_lines, sum([score_line(line) for line in rotate(tmp_lines)])


# Initial rotation
grid = lines
scores = []
for _ in range(1000):
    grid, score = cycle(grid)
    scores.append(score)
print(scores)


# 105637 is too high
