import os
import shutil

from diffimg import diff
from PIL import Image

from constants import BOTTOM, LEFT, RIGHT, SQUARE_WIDTH, TOP

knowns = {
    1: "images/1/average.png",
    2: "images/2/average.png",
    3: "images/3/average.png",
    4: "images/4/average.png",
    5: "images/5/average.png",
    6: "images/6/average.png",
    7: "images/7/average.png",
    8: "images/8/average.png",
    9: "images/9/average.png",
    "empty": "images/empty/average.png",
}


def get_number(unknown):
    """
    Compare an unknown image to a known image and extract the number

    :param unknown: The path to the unknown image
    :type unknown: str

    :return: The number contained in the unknown image or None if it is empty
    :rtype: int or None
    """
    ratios = {
        num: diff(known, unknown, delete_diff_file=True)
        for num, known in knowns.items()
    }
    num = min(ratios, key=ratios.get)
    return num if num != "empty" else None


def get_board(image, clean_up=True):
    """
    Convert image into grid using Python data types

    :param image: The image to split up into cells
    :type image: PIL.Image

    :param clean_up: Whether or not to remove temp files (default = True)
    :type clean_up: bool

    :return: A tiple containing the image-based board and the Python interpretation
    :rtype: tuple[PIL.Image, list[list[int]]]
    """
    os.makedirs("tmp", exist_ok=True)

    matrix = [[None for i in range(9)] for j in range(9)]

    board = image.crop((LEFT, TOP, RIGHT, BOTTOM))
    for row in range(9):
        for column in range(9):
            top = row * SQUARE_WIDTH
            bottom = (row + 1) * SQUARE_WIDTH
            left = column * SQUARE_WIDTH
            right = (column + 1) * SQUARE_WIDTH

            square = board.crop((left, top, right, bottom))
            square.save(f"tmp/{row}{column}.png")

            number = get_number(f"tmp/{row}{column}.png")
            matrix[row][column] = number

    if clean_up:
        shutil.rmtree("tmp")

    return board, matrix
