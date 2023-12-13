import numpy as np

with open("11/input.txt") as f:
    lines = [line.rstrip() for line in f]

mat = np.array([[(0 if c == "." else 1) for c in line] for line in lines])

empty_rows = [r for r, val in enumerate(mat) if np.sum(val) == 0]
empty_cols = [r for r, val in enumerate(np.transpose(mat)) if np.sum(val) == 0]
n_new_rows = np.size(mat, 0) + len(empty_rows)
n_new_cols = np.size(mat, 1) + len(empty_cols)

new_grid = np.zeros((n_new_rows, n_new_cols))

mat = [np.insert(mat, row, mat[row]) for row in empty_rows]
print(mat)
