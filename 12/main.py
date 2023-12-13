from math import comb

with open("12/input.txt") as f:
    lines = [line.rstrip() for line in f]

problems = []
for line in lines:
    raw, inp = line.split()
    inp = [int(x) for x in inp if x.isnumeric()]
    rows = [n for n in raw.split(".") if n]
    problems.append((rows, inp))

print(((7 - 3) ** 2 + 4) / 2)
print(comb(5, 2))


def two_into_n(n, a, b):
    return comb(n - (a + b) + 1, 2)


def three_into_n(n, a, b, c):
    return sum([two_into_n(n - c, a, b) for n in range(c + 1, a + b + 2)])


print(two_into_n(9, 2, 3))
print(three_into_n(100, 1, 1, 1))

# Separate problem into different P1s


def P2(rows, inp):
    print(f"Problem is {['?'*r for r in rows]} : {inp}")

    to_split = inp[-1] if type(inp[-1]) == list else inp
    print(f"\n")

    solutions = []
    for i in range(len(to_split)):
        span = to_split[:i]
        span_fits = len(span) + sum(span) <= rows[0]
        if span_fits:
            remainder = to_split[i:]
            solutions.append([span, remainder])
            print(f"result found! {span, remainder}")
    print(f"The new solutions are {solutions[0]}")
    print(f"solutions are {rows}")
    if len(rows) > 1:
        for sol in solutions:
            print(f"solution is {sol}")
            sol.append(P2(rows[1:], sol[1]))
    print(f"Result was {solutions}")
    return solutions


# rows: [4, 2, 1, 8]  inp: [1 1 1 4]
rows = [4, 2, 2]
inp = [1, 1, 1]


res = P2(rows, [1, 1, 1])
print("results: \n")
for r in res:
    if len(r) == 3:
        print("subsolution found: ")
        for x in r:
            print(r)

# print(problems)
