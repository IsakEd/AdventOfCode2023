import numpy as np

with open("2/input.txt") as f:
    lines = [line.rstrip() for line in f]

print(lines[0])
limits = {"red": 12, "green": 13, "blue": 14}


def is_valid_game(line: str):
    game_sets = line.split(":")[1].split(";")
    for gset in game_sets:
        combos = gset.strip().split(",")
        for combo in combos:
            amount, color = combo.strip().split(" ")
            if int(amount) > limits[color]:
                return False
    return True


def highest_amount_balls(line: str):
    game_sets = line.split(":")[1].split(";")
    max_balls = {k: 0 for k in limits}
    for gset in game_sets:
        combos = gset.strip().split(",")
        for combo in combos:
            amount, color = combo.strip().split(" ")
            if int(amount) > max_balls[color]:
                max_balls[color] = int(amount)
    return max_balls


# P1
print(sum([(i + 1) for i, line in enumerate(lines) if is_valid_game(line)]))

# P2
print(sum([np.prod(list(highest_amount_balls(line).values())) for line in lines]))
