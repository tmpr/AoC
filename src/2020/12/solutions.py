from dataclasses import dataclass

import numpy as np
from numpy.linalg import norm

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

@dataclass
class Ferry:
    direction : int = EAST
    coords : np.array = np.array([0, 0])

    moves = {
        'E': np.array([1, 0]),
        'N': np.array([0, 1]),
        'W': np.array([-1, 0]),
        'S': np.array([0, -1])
    }

    dirs = {
        0 : 'E',
        90 : 'N',
        180 : 'W',
        270 : 'S'
    }

    def move(self, command):
        letter, arg = command[0], int(command[1:])
        if letter == "F":
            self.coords += Ferry.moves[Ferry.dirs[self.direction]] * arg
        elif letter == "R":
            self._turn(-arg)
        elif letter == "L":
            self._turn(arg)
        else: 
            self.coords += Ferry.moves[letter] * arg
    
    @property
    def manh_dist(self):
        return sum(abs(self.coords))

    def _turn(self, degrees):
        """Turn a given amount of degrees."""
        self.direction = (self.direction + degrees) % 360
        if self.direction < 0:
            self.direction = (-self.direction) + 180

@dataclass
class WPFerry(Ferry):
    direction : int = EAST
    coords : np.array = np.array([0, 0])
    wp : np.array = np.array([10, 1])

    def move(self, command):
        letter, arg = command[0], int(command[1:])
        if letter == "F":
            change = (self.wp - self.coords) * arg
            self.wp += change
            self.coords += change
        elif letter == "R":
            self.wp = rel_orth_vector(self.coords, self.wp, -arg)
        elif letter == "L":
            self.wp = rel_orth_vector(self.coords, self.wp, arg)
        else: 
            self.wp += Ferry.moves[letter] * arg


def rel_orth_vector(point, rotator, deg):
    """Let one point rotate 90 degrees around another."""
    if deg in {180, -180}:
        return 2*point - rotator
    elif deg in {-360, 360}:
        return rotator
    else: 
        diff = np.flip(point - rotator)
        if deg in {270, -90}:
            diff[0] *= -1
        elif deg in {-270, 90}:
            diff[1] *= -1
        return point + diff
    

def part_1(input_data: str):
    """Return first solution of puzzle."""
    ferry = Ferry()
    for instruction in input_data.splitlines():
        ferry.move(instruction)
    return ferry.manh_dist

def part_2(input_data: str):
    """Return second solution of puzzle."""
    ferry = WPFerry()
    for instruction in input_data.splitlines():
        ferry.move(instruction)
    return ferry.manh_dist
