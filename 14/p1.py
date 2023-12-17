with open("14/input.txt") as f:
    lines = [line.rstrip() for line in f]


def rotate(lines):
    return ["".join(t)[::-1] for t in [*zip(*lines)]]


def slide(grid):
    def slide_seg(seg: str):
        n = sum([(c == "O") for c in seg])
        return "." * (len(seg) - n) + "O" * n

    def slide_line(line):
        segments = [[slide_seg(seg) for seg in line.split("#")]]
        new_line = "#".join(*segments)
        return new_line

    return [slide_line(line) for line in grid]


def score_grid(grid):
    total = 0
    for line in grid:
        total += sum(i + 1 for i, ch in enumerate(line) if ch == "O")
    return total


def cycle(grid):
    for _ in range(4):
        grid = slide(rotate(grid))
    return grid


p1 = score_grid(slide(rotate(lines)))
print(cycle(lines))

grid = lines
scores = []
for i in range(1000):
    grid = cycle(grid)
    scores.append(score_grid(grid))
print(scores)
