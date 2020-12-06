from functools import reduce

def part_1(input_data: str):
    """Return first solution of puzzle."""
    return sum(len(set(line).difference({'\n'}))
                for line in input_data.split('\n\n'))
    

def part_2(input_data: str):
    """Return second solution of puzzle."""
    return sum(len(reduce(lambda a,b: a&b, (set(l) for l in line.splitlines()))) - {'\n'} 
                    for line in input_data.split('\n\n'))
    