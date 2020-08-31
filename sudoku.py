"""
The bulk of this file was adapted from https://github.com/jjallan/sudoku/blob/master/sudoku.py

See below for original license:

Copyright (c) 2019 Jonathan Allan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from itertools import chain

import dlx

from constants import SQUARE_SIZE, SUDOKU_SIZE, NUM_CELLS


def contraint_indexes_from_candidate(row, column, value):
    """
    Honestly, no idea what this function does, but it is used below and in the dlx algorithm

    :param row: The row number (0-8)
    :type row: int

    :param column: The column number (0-8)
    :type column: int

    :param value: The value for this column (1-9)
    :type value: int

    :return: I don't even know, dude
    :rtype: tuple[int]
    """
    first = SUDOKU_SIZE * row + column
    second = NUM_CELLS + SUDOKU_SIZE * row + value - 1
    third = NUM_CELLS * 2 + SUDOKU_SIZE * column + value - 1
    fourth = (
        NUM_CELLS * 3
        + SUDOKU_SIZE * (SQUARE_SIZE * (row // SQUARE_SIZE) + column // SQUARE_SIZE)
        + value
        - 1
    )

    return (first, second, third, fourth)


# The order of these is important, as they depend on one another
CANDIDATES = [
    (row, column, value)
    for row in range(SUDOKU_SIZE)
    for column in range(SUDOKU_SIZE)
    for value in range(1, SUDOKU_SIZE + 1)
]
CONSTRAINT_FORMATTERS = ["R{0}C{1}", "R{0}#{1}", "C{0}#{1}", "B{0}#{1}"]
CONSTRAINT_NAMES = [
    (string.format(row, column + (i and 1)), dlx.DLX.PRIMARY)
    for i, string in enumerate(CONSTRAINT_FORMATTERS)
    for row in range(SUDOKU_SIZE)
    for column in range(SUDOKU_SIZE)
]
EMPTY_GRID_CONSTRAINT_INDEXES = [
    contraint_indexes_from_candidate(row, column, value)
    for (row, column, value) in CANDIDATES
]


class Sudoku:
    def __init__(self, board):
        """
        Initialize a Sudoku object

        :param board: A 2D list representing the board to solve
        :type board: list[list[int]]
        """
        # Convert our 2D array into 1D for use in dlx
        self._repr = list(chain(*board))

        # Initialize our dlx instance with the outside vars
        self._dlx = dlx.DLX(CONSTRAINT_NAMES)
        row_indexes = self._dlx.appendRows(EMPTY_GRID_CONSTRAINT_INDEXES, CANDIDATES)
        for row in range(SUDOKU_SIZE):
            for column in range(SUDOKU_SIZE):
                value = self._repr[SUDOKU_SIZE * row + column]
                if value:
                    self._dlx.useRow(
                        row_indexes[NUM_CELLS * row + SUDOKU_SIZE * column + value - 1]
                    )

    def solve(self):
        """
        Solve the sudoku contained in this object in place
        """
        # dlx will find all possible solutions. A "proper" sudoku will only have one solution.
        # Since we are using a sudoku app, we can assume properness and just take the first
        solution = list(self._dlx.solve(dlx.DLX.smallestColumnSelector))[0]
        self._repr = [
            value for (row, column, value) in sorted([self._dlx.N[i] for i in solution])
        ]

    def __str__(self):
        """
        Convert the sudoku contained in this object to a pretty string for printing

        This is specific to the iPhone XR, so all the hard-coded values are to center
        on that screen
        """
        _2d = [
            self._repr[i : i + SUDOKU_SIZE] for i in range(0, NUM_CELLS, SUDOKU_SIZE)
        ]
        output = "\n"  # Always start on a new line

        def horizontal_line():
            return "------+-------+------".rjust(34) + "\n"

        for i, row in enumerate(_2d):
            for j, column in enumerate(row):
                char = str(column) if column else "•"
                end = " " if j != 8 else "\n"
                if j == 0:
                    output += f"{char: >14}{end}"
                elif j in (3, 6):
                    output += f"| {char}{end}"
                else:
                    output += f"{char}{end}"

            if i in (2, 5):
                output += horizontal_line()

        return output
