import numpy as np

with open("4/input.txt") as f:
    lines = [line.rstrip() for line in f]


def score(line: str):
    bin, win = [b.strip().split(" ") for b in line.split("|")]
    bin = [b for b in bin[2:] if b]
    win = [w for w in win if w]
    print(bin, win)
    n_matches = sum([b in win for b in bin if b])
    print(f"Matches: {n_matches}")
    return 2 ** (n_matches - 1) if n_matches else 0


def n_matches(line: str):
    bin, win = [b.strip().split(" ") for b in line.split("|")]
    bin = [b for b in bin[2:] if b]
    win = [w for w in win if w]
    n_matches = sum([b in win for b in bin if b])
    return n_matches


def add_card_amounts(n_matches: int, index: int, amount_cards: list):
    indices_to_raise = range(int(i) + 1, int(i) + 1 + n_matches)
    amount_to_raise = amount_cards[index]

    for idx in indices_to_raise:
        if idx < len(lines):
            amount_cards[idx] += amount_to_raise


# P1
print(sum([score(l) for l in lines]))

# P2
amount_cards = [1] * len(lines)

for i, card in enumerate(lines):
    add_card_amounts(n_matches(card), i, amount_cards)

print(sum(amount_cards))
