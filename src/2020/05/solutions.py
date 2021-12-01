def bisect(array: list, u=True) -> list:
    mid = len(array) // 2
    return array[:mid] if not u else array[mid:]


def seat_id(row: int, col: int) -> int:
    return (row * 8) + col


def calc_seat_id(code: str) -> int:
    rows = list(range(128))
    cols = list(range(8))
    for c in code[:7]:
        rows = bisect(rows, c == "B")
    for c in code[7:]:
        cols = bisect(cols, c == "R")
    return seat_id(rows[0], cols[0])


def part_1(input_data: str):
    """Return first solution of puzzle."""
    return max(calc_seat_id(line) for line in input_data.splitlines())


def part_2(input_data: str):
    """Return second solution of puzzle."""
    ids = list(calc_seat_id(line) for line in input_data.splitlines())
    max_ = max(ids)

    print(set(range(-1, max_)) - set(ids))
    # Pretty manual solution but idk how to compute that algorithmically :D
    return int(input("Enter number at that sticks out: "))
