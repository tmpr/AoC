from itertools import combinations
from functools import reduce
from operator import mul

def mul_summands(input_data: str, n_summands: int) -> int:
    """Find summands of 2020 and return their product."""
    numbers = [int(n) for n in input_data.splitlines()]
    for comb in combinations(numbers, n_summands):
        if sum(comb) == 2020:
            return reduce(mul, comb)


def part_1(input_data: str) -> int:
    return mul_summands(input_data, 2)


def part_2(input_data: str) -> int:
    return mul_summands(input_data, 3)
