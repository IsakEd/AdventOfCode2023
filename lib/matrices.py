from itertools import product


def get_adjacent_positions(col_start_idx: int, row_idx: int, length: int, shape):
    word_positions = set(
        [(row_idx, c) for c in range(col_start_idx, col_start_idx + length + 1)]
    )

    col_span = set(range(col_start_idx - 1, col_start_idx + length + 1)).intersection(
        set(range(shape[0]))
    )

    row_span = set(range(col_start_idx - 1, col_start_idx + 2)).intersection(
        set(range(shape[1]))
    )
    positions = set([(r, c) for r, c in product(row_span, col_span)])
    return positions.difference(word_positions)
