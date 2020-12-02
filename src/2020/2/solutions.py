import re

RULE_PATTERN = re.compile(r'(\d*)-(\d*) (.)')

def password_policies(input_data, part_a=True):
    found = 0
    for line in input_data.splitlines():
        
        rule = re.match(RULE_PATTERN, line)
        low = int(rule.group(1))
        high = int(rule.group(2))
        letter = rule.group(3)
        
        rule = re.compile('\d*-\d* ' + letter + ': (.*)')
        valid = re.search(rule, line)
        letters = valid.group(1)

        if part_a:
            found += bool(low <= letters.count(letter) <= high)
        else:
            found += bool(letters[low - 1] == letter 
                          and letters[high - 1] != letter)

    return found

def part_1(input_data: str):
    """Return first solution of puzzle."""
    return password_policies(input_data)



def part_2(input_data: str):
    """Return second solution of puzzle."""
    return password_policies(input_data, part_a=False)