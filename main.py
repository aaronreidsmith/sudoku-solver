import sys

import appex

from sudoku import Sudoku
from utils import get_board


if not appex.is_running_extension():
    print("Must use share sheet to pass in image!")
    sys.exit(1)

image = appex.get_image()
orig, grid = get_board(image)

print("Original".center(45))
orig.show()

sudoku = Sudoku(grid)
print("\n", "Interpreted".center(45), sudoku)

sudoku.solve()
print("Solved".center(45), sudoku)
