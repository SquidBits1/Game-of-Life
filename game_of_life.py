import numpy as np
import random

DEAD = 0
ALIVE = 1
ALIVE_PROBABILITY = 0.1

def generate_grid(length, alive_probability):
    """
    Make a grid of specified shape with cells randomly set to one or zero, with probabillity p. 
    Inputs:
      length (integer) - The size of the grid. The grid will be a square with width and height of magnitude length.
      alive_probability (float) - The probability that any given cell is set to alive.
    """
    grid = (np.random.random((length,length)) < alive_probability).astype(np.int8)
    return grid
def update_grid(old_grid, rule=None):
    pass

def update_cell(cell_section: np.array):
    centre = cell_section[1,1]
    neightbours = cell_section
    neightbours[1,1] = 0
    c = np.count_nonzero(neightbours == 1)
    if c == 0:
        centre = 0
    if c == 1:
        centre = 0
    if c == 2 and centre == 1:
        centre = 1
    if c == 2 and centre == 0:
        centre = 0
    if c == 3:
        centre = 1
    if c >=4:
        centre = 0
    
    return centre
def display_grid(grid):
    pass

def test_update_grid():
    pass

def test_update_cell():
    assert(update_cell(np.array([[0,0,0],[0,0,0],[0,0,0]]))) == 0
    assert(update_cell(np.array([[0,0,0],[0,1,0],[0,0,0]]))) == 0
    assert(update_cell(np.array([[0,1,0],[0,0,0],[0,0,0]]))) == 0
    assert(update_cell(np.array([[0,1,0],[0,1,0],[0,0,0]]))) == 0
    assert(update_cell(np.array([[0,1,0],[0,0,0],[0,1,0]]))) == 0
    assert(update_cell(np.array([[0,1,0],[0,1,0],[0,1,0]]))) == 1
    assert(update_cell(np.array([[0,1,0],[1,0,0],[0,1,0]]))) == 1
    assert(update_cell(np.array([[0,1,0],[1,1,0],[0,1,0]]))) == 1
    assert(update_cell(np.array([[0,1,0],[1,0,1],[0,1,0]]))) == 0
    assert(update_cell(np.array([[0,1,0],[1,1,1],[0,1,0]]))) == 0
    

def main():
    update_cell(np.array([[0,1,0],[0,1,0],[0,0,0]]))
    test_update_cell()

main()
