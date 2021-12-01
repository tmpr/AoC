import re

FIELDS = {
    "byr:",  # (Birth Year)
    "iyr:",  # (Issue Year)
    "eyr:",  # (Expiration Year)
    "hgt:",  # (Height)
    "hcl:",  # (Hair Color)
    "ecl:",  # (Eye Color)
    "pid:",  # (Passport ID)
    # "cid", #(Country ID)
}


PATTERNS = [
    re.compile(r"byr:" + "(" + "".join(f"{n}|" for n in range(1920, 2003))[:-1] + ")"),
    re.compile(r"iyr:" + "(" + "".join(f"{n}|" for n in range(2010, 2021))[:-1] + ")"),
    re.compile(r"eyr:" + "(" + "".join(f"{n}|" for n in range(2020, 2031))[:-1] + ")"),
    re.compile(
        r"hgt:"
        + "("
        + "".join(f"{n}cm|" for n in range(150, 194))  # Centimeters
        + "".join(f"{n}in|" for n in range(59, 77))[:-1]  # Inches
        + ")"
    ),
    re.compile(r"hcl:#[0-9a-f]{6}"),
    re.compile(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)"),
    re.compile(r"pid:(\d{9}(.|\n)|\d{9}$)"),
]


def part_1(input_data: str) -> int:
    """Return first solution of puzzle."""
    lines = input_data.split("\n\n")
    return sum(all(field in line for field in FIELDS) for line in lines)


def part_2(input_data: str) -> int:
    """Return second solution of puzzle."""
    lines = input_data.split("\n\n")
    return sum(all(re.search(pat, line) for pat in PATTERNS) for line in lines) - 1
