import typing as t


def part_1(input_data: str) -> int:
    """Return first solution of puzzle."""
    numbers = list(map(int, input_data.splitlines()))
    return count_increases(numbers)


def part_2(input_data: str) -> int:
    """Return second solution of puzzle."""
    numbers = list(map(int, input_data.splitlines()))
    return count_increases(triple_sums(numbers))


def count_increases(seq: t.Sequence[int]) -> int:
    return sum(a < b for a, b in pairwise(seq))


def triple_sums(seq: t.Sequence[int]) -> t.Sequence[int]:
    return list(map(sum, list(zip(seq, seq[1:], seq[2:]))))


def pairwise(seq: t.Sequence) -> t.List[t.Tuple[int, int]]:
    return list(zip(seq, seq[1:]))
