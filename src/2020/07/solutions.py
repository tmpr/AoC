import re

PAT = re.compile(r'(.*) bags contain (.*)')


def bag_entry(left):
    entry = [
        (int(s[0]), s[1] + (' ' + s[2] if len(s) == 4 else ''))
        for comma in left.split(',') if (s := comma.split())
        and not comma.startswith('no')
    ]
    return entry


def build_bag_map(input_data):
    rules = input_data.splitlines()
    matches = (re.match(PAT, rule) for rule in rules)
    bag_map = {match.group(1): bag_entry(match.group(2))
               for match in matches}
    return bag_map


def contain(bags, key, col='shiny gold'):
    return any(bcol == col or contain(bags, bcol, col)
               for num, bcol in bags[key])


def size(bags, key):
    return sum(num * (size(bags, bcol) + 1)
               for num, bcol in bags[key])


def part_1(input_data: str):
    """Return first solution of puzzle."""
    bag_map = build_bag_map(input_data)
    return sum(
        contain(bag_map, key) for key in bag_map)


def part_2(input_data: str):
    """Return second solution of puzzle."""
    bag_map = build_bag_map(input_data)
    return size(bag_map, 'shiny gold')
