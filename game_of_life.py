"""
by Rocco and Gilad
"""

import numpy as np
import random
import matplotlib.pyplot as plt


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
def update_grid(old_grid, length=5,rule=None):
    new_grid = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
    cell_section = np.array([[0,0,0],[0,0,0],[0,0,0]])
    for y in range(len(old_grid)):
        for x in range(len(old_grid[0])):
            #create cell section
            for i in range(3):
                for j in range(3):
                    place_y = (x+i-1)%length
                    place_x = (y+j-1)%length
                    cell_section[j,i] = old_grid[place_x,place_y]
            c = update_cell(cell_section)
            new_grid[y,x] = c
    return new_grid
    #acc update now

def update_cell(cell_section: np.array):
    centre = cell_section[1,1]
    neighbours = cell_section
    neighbours[1,1] = 0
    c = np.count_nonzero(neighbours == 1)
    if c <= 1:
        return 0
    if c == 2:
        return centre
    if c == 3:
        return 1
    if c >= 4:
        return 0
def display_grid(grid):
    pass




def test_update_grid():
    #assert(update_grid(np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))) == ([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
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
    grid = generate_grid(5,0.1)
    #update_grid(grid)
    test = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
    print(test)
    print(update_grid(test))
    
main()
