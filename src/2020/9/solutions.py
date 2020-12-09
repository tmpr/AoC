from itertools import accumulate
from collections import deque
from copy import deepcopy


def part_1(input_data: str, n_preamb=25):
    """Return first solution of puzzle."""
    data = [int(n) for n in input_data.splitlines()]
    preamble = deque(data[:n_preamb], maxlen=n_preamb)
    for y in data[n_preamb:]:
        if any(y - x in preamble for x in preamble if x+x != y):
            preamble.append(y)
        else:
            return y


def part_2(input_data: str, n_preamb=25):
    """Return second solution of puzzle."""
    inv_n = part_1(input_data, n_preamb)
    data = [int(n) for n in input_data.splitlines()]

    for sub_l in sublists(data):
        acc = list(accumulate(sub_l))
        if inv_n in acc:
            contiguous = sub_l[:acc.index(inv_n)]
            return min(contiguous) + max(contiguous)


def sublists(data):
    return (data[i:] for i in range(len(data)))
