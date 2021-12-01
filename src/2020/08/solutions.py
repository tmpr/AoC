from .handheld import HandHeld


def part_1(input_data: str):
    """Return first solution of puzzle."""
    hh = HandHeld()
    return hh.run(input_data.splitlines())


def part_2(input_data: str):
    """Return second solution of puzzle."""
    hh = HandHeld()
    return hh.repaired_run(input_data.splitlines())
