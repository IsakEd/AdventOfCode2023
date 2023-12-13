import itertools as it
import collections as co
import numpy as np

with open("7/input.txt") as f:
    lines = [line.rstrip() for line in f]


hands = []
bids = []


def value(card):
    card_strength = "23456789TJQKA"
    return card_strength.index(card) + 1


def sec_value(hand):
    val = ""
    for i, c in enumerate(hand):
        val += str((value(c) + 10))
    return int(val)


def score(hand):
    counts = co.Counter(hand)
    hicard = counts.most_common()
    print(sec_value(hand))
    print(hicard)
    if hicard[0][1] == 5:
        return 7
    elif hicard[0][1] == 4:
        return 6
    elif hicard[0][1] == 3 and hicard[1][1] == 2:
        return 5  # fullhouse
    elif hicard[0][1] == 3:
        return 3
    elif hicard[0][1] == 2:
        return 2
    elif hicard[0][1] == 1:
        return 1


handbids = [l.split(" ") for l in lines]
print(handbids)
handbids.sort(key=lambda x: (score(x[0]), sec_value(x[0])))

total_winnings = 0

for i, hb in enumerate(handbids):
    print(hb)
    hand, bid = hb
    total_winnings += int(bid) * (i + 1)


print(total_winnings)
245847558
