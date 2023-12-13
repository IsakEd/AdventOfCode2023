import numpy as np

with open("6/input.txt") as f:
    lines = [line.rstrip() for line in f]

times = [int(j) for j in lines[0].split(" ")[1:] if j]
dists = [int(j) for j in lines[1].split(" ")[1:] if j]


def dist(tc, ts):
    return tc * ts - tc * tc


n_winners = []
for t_stop, d in zip(times, dists):
    scores = [dist(tc, t_stop) for tc in range(0, t_stop)]
    n_winners.append(sum([int(score > d) for score in scores]))

print(np.prod(n_winners))

# P2
time = int("".join([str(t) for t in times]))
d = int("".join(str(d) for d in dists)) + 1  # +1 to win
print(time, d)

print(-1 * time / d)

win_tc_low = (time / 2) - np.sqrt((time / 2) ** 2 - d)
win_tc_high = (time / 2) + np.sqrt((time / 2) ** 2 - d)
res = int(win_tc_high - win_tc_low)


print(res)

print(sum([dist(tc, time) >= d for tc in range(time)]))
