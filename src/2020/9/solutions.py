from itertools import accumulate


def part_1(input_data: str, n_preamb=25):
    """Return first solution of puzzle."""
    data = [int(n) for n in input_data.splitlines()]

    for i, number in enumerate(data[n_preamb:]):
        preamble = data[i:i+n_preamb]
        if any(number - x in preamble for x in preamble):
            continue
        else:
            return number


def part_2(input_data: str, n_preamb=25):
    """Return second solution of puzzle."""
    inv_n = part_1(input_data, n_preamb)
    data = [int(n) for n in input_data.splitlines()]

    for slice_ in slices(data):
        acc = list(accumulate(slice_))
        if inv_n in acc:
            right = acc.index(inv_n)
            return min(slice_[:right]) + max(slice_[:right])


def slices(input_data):
    for i in range(len(input_data)):
        yield input_data[i:]
