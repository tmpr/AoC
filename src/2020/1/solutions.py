from itertools import combinations
from functools import reduce
from operator import mul

def part_1(input_data: str, n_summands=2):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    numbers = [int(line) for line in input_data.splitlines()]
    for comb in combinations(numbers, n_summands):
        if sum(comb) == 2020:
            return reduce(mul, comb)


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    return part_1(input_data, n_summands=3)
