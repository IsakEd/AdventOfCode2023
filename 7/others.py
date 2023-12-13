from functools import cmp_to_key
import collections
import itertools


def parse(task_input):
    for line in task_input:
        t = line.split()
        yield t[0], int(t[1])

    return


FIVE_OF_KIND = 7
FOUR_OF_KIND = 6
FULL_HOUSE = 5
THREE_OF_KIND = 4
TWO_PAIRS = 3
ONE_PAIR = 2
HIGH_CARD = 1


def get_value_card(hand):
    individual_cards = collections.Counter(hand)

    if len(individual_cards) == 1:
        return FIVE_OF_KIND

    if len(individual_cards) == 2:
        if 3 in individual_cards.values():
            if 2 in individual_cards.values():
                return FULL_HOUSE

        if 4 in individual_cards.values():
            return FOUR_OF_KIND

        raise Exception("?")

    if len(individual_cards) == 3:
        if 3 in individual_cards.values():
            return THREE_OF_KIND

        s = 0
        for c, i in individual_cards.items():
            if i == 2:
                s += 1

        if s == 2:
            return TWO_PAIRS

    if 2 in individual_cards.values():
        return ONE_PAIR

    return HIGH_CARD


def get_hand_combinations(prefix, index, hand, possibilities):
    if index == 5:
        yield prefix
        return

    if hand[index] == "J":
        for p in possibilities:
            yield from get_hand_combinations(prefix + p, index + 1, hand, possibilities)
    else:
        yield from get_hand_combinations(
            prefix + hand[index], index + 1, hand, possibilities
        )


def get_value_card_with_jokers(hand):
    if "J" not in hand:
        return get_value_card(hand)

    if hand == "JJJJJ":
        return FIVE_OF_KIND

    possibilities = set(c for c in hand if c != "J")
    return max(
        get_value_card(h) for h in get_hand_combinations("", 0, hand, possibilities)
    )


def compare_for_first_part(item1, item2):
    CARD_VALUES = {c: b for c, b in zip("AKQJT98765432"[::-1], itertools.count(1))}

    t1 = get_value_card(item1[0])
    t2 = get_value_card(item2[0])

    if t1 > t2:
        return 1

    if t1 < t2:
        return -1

    for c1, c2 in zip(item1[0], item2[0]):
        if c1 == c2:
            continue

        return CARD_VALUES[c1] - CARD_VALUES[c2]

    return 0


def compare_for_second_part(item1, item2):
    CARD_VALUES = {c: b for c, b in zip("AKQT98765432J"[::-1], itertools.count(1))}

    t1 = get_value_card_with_jokers(item1[0])
    t2 = get_value_card_with_jokers(item2[0])

    if t1 > t2:
        return 1

    if t1 < t2:
        return -1

    for c1, c2 in zip(item1[0], item2[0]):
        if c1 == c2:
            continue

        return CARD_VALUES[c1] - CARD_VALUES[c2]

    return 0


def solution_for_first_part(task_input):
    lines = list(parse(task_input))
    result = 0

    for (hand, bid), index in zip(
        sorted(lines, key=cmp_to_key(compare_for_first_part)), itertools.count(1)
    ):
        result += index * bid

    return result


def solution_for_second_part(task_input):
    lines = list(parse(task_input))
    result = 0

    for (hand, bid), index in zip(
        sorted(lines, key=cmp_to_key(solution_for_second_part)), itertools.count(1)
    ):
        result += index * bid

    return result


with open("7/input.txt") as f:
    task_input = [line.rstrip() for line in f]
print("Solution for the first part:", solution_for_first_part(task_input))
