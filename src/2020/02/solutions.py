import re

from operator import xor

RULE_PATTERN = re.compile(r"(\d*)-(\d*) (.): (.*)")


def password_policies(input_data, part_a=True):
    found = 0
    for line in input_data.splitlines():

        rule = re.match(RULE_PATTERN, line)
        low = int(rule.group(1))
        high = int(rule.group(2))
        letter = rule.group(3)
        letters = rule.group(4)

        if part_a:
            found += low <= letters.count(letter) <= high
        else:
            found += xor(letters[low - 1] == letter, letters[high - 1] == letter)

    return found


def part_1(input_data: str):
    """Return first solution of puzzle."""
    return password_policies(input_data)


def part_2(input_data: str):
    """Return second solution of puzzle."""
    return password_policies(input_data, part_a=False)
