from itertools import product, combinations

with open("11/input.txt") as f:
    mat = [line.rstrip() for line in f]

coeff = 1_000_000
n_rows, n_cols = len(mat), len(mat[0])

stars = [
    complex(r, c) for r, c in product(range(n_rows), range(n_cols)) if mat[r][c] == "#"
]

nil_rows = set(range(n_rows)) - set([c.real for c in stars])
nil_cols = set(range(n_cols)) - set([c.imag for c in stars])

expanded = []
# for each point, add the amount of empty rows before it to itself
for dot in stars:
    n_preceding_rows = sum([s < dot.real for s in nil_rows])
    n_preceding_cols = sum([s < dot.imag for s in nil_cols])
    print(n_preceding_cols)
    expanded.append(dot + complex(coeff * n_preceding_rows, coeff * n_preceding_cols))


def manhattan(z1, z2):
    return abs(z1.real - z2.real) + abs(z1.imag - z2.imag)


print(sum([manhattan(a, b) for a, b in combinations(expanded, 2)]))

print(1112 - 1030)
print(8492 - 8410)
print(904633799472 - 904634704098)
print(9608724 / 904626)
print(len(dots))
print(9608724 / len(dots))
