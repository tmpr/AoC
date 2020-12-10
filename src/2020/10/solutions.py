import numpy as np
from collections import Counter
from copy import deepcopy
from itertools import takewhile
from functools import lru_cache


def part_1(input_data: str):
    """Return first solution of puzzle."""
    adapters = [int(n) for n in input_data.splitlines()] + [0]
    adapters.append(max(adapters)+3)
    adapters = np.array(sorted(adapters))

    counts = Counter(np.diff(adapters))
    return counts[3] * counts[1]

def backsearch(change_map):
    return change_map[-1] == 0 or sum(backsearch(change_map[:-1-i]) for i 
                                                in range(change_map[-1]))



def part_2(input_data: str):
    """Return second solution of puzzle."""
    # Backwards Tree Search Basically
    adapters = [int(n) for n in input_data.splitlines()] + [0]
    adapters.append(max(adapters)+3)
    change_map = tuple(sum(1 <= i - j <= 3 for j in adapters) 
                  for i in sorted(adapters))
    return backsearch(change_map)