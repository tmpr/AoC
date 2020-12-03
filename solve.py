from importlib import import_module
from aocd.models import Puzzle

from fire import Fire


def solve(day, year=2020, submit=True):
    sol = import_module(f'src.{year}.{day}.solutions')
    puzzle = Puzzle(int(year), int(day))
    answer_a = sol.part_1(puzzle.input_data)
    if submit:
        puzzle.answer_a = answer_a
    answer_b = sol.part_2(puzzle.input_data)
    if submit:
        puzzle.answer_b = answer_b


if __name__ == "__main__":
    Fire(solve)
