with open("8/input.txt") as f:
    lines = [line.rstrip() for line in f]

instructions = lines[0] * 1000000000
keymap = {}
names = [l.split(" = ")[0] for l in lines[2:]]

for line, name in zip(lines[2:], names):
    n, tupstr = line.split(" = ")
    L, R = tupstr[1:4], tupstr[-4:-1]
    keymap[name] = [names.index(L), names.index(R)]


def find_next(current_name: str, i: int):
    instruction = 0 if instructions[i] == "L" else 1
    next_name = names[keymap[current_name][instruction]]
    return next_name


next_name = "AAA"
iterations = 0
while True:
    next_name = find_next(next_name, iterations)
    if next_name == "ZZZ":
        break
    iterations += 1

print(iterations + 1)
