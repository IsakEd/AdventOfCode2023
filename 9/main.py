import numpy as np

with open("9/input.txt") as f:
    lines = [line.rstrip() for line in f]

signals = [np.array([int(num) for num in line.split(" ")]) for line in lines]


def predict(signal: np.array):
    current_level = signal[::-1]
    rows = [current_level]
    while not all([x == 0 for x in current_level]):
        current_level = np.diff(current_level)
        rows.append(current_level)
    return sum([arr[-1] for arr in rows])


print(sum([predict(signal) for signal in signals]))
