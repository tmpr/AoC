import re

from operator import mul
from functools import reduce

import numpy as np


def string_to_matrix(input_data):
    return np.array([
        np.array([char for char in line])
        for line in input_data.splitlines()])


def part_1(input_data: str, dv=3, dh=1):
    """Return first solution of puzzle."""
    
    field = string_to_matrix(input_data)
    height, width = field.shape
    n_trees = 0
    v = 0
    
    for h in range(0, height, dh):
        n_trees += field[h][v] == '#'
        v += dv
        v %= width

    return n_trees


def part_2(input_data: str):
    """Return second solution of puzzle."""
    configs = (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
    return reduce(mul, (part_1(input_data, *config) for config in configs))
