import numpy as np
import networkx as nx

from scipy.signal import convolve2d


EMPTY = 'L'
OCCUP = '#'
FLOOR = '.'

ADJKERNEL = np.array([
    [1,   1, 1],
    [1, 9, 1],
    [1,   1, 1]
])

class SeatingRoom:

    def __init__(self, input_data):
        self.room = np.array([[char for char in row] 
                              for row in input_data.splitlines()])
        self.floor = self.room == FLOOR
        self.room = self.room == OCCUP
    
    def step(self):
        temp = convolve2d(self.room, ADJKERNEL, mode='same')
        self.room = (self.room + (temp == 0)) * (temp <= 12) * ~self.floor 
    
    def converge(self, b=False):
        old_room = 'dummy'
        while np.any(self.room != old_room):
            print
            old_room = self.room.copy()
            self.step()
        return sum(n for row in self.room for n in row)


def part_1(input_data: str):
    """Return first solution of puzzle.""" 
    return SeatingRoom(input_data).converge()
    

def part_2(input_data: str):
    """Return second solution of puzzle."""
    raise NotImplementedError