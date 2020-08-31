import sys

import appex

if not appex.is_running_extension():
    print('This has to be run from the share sheet')
    sys.exit(1)

image = appex.get_image()

# Same values as ../constants.py, but this was a throway script written first
left = 18
right = 810
top = 393
bottom = 1185
board = image.crop((left, top, right, bottom))

# Crop all 81 squares from the above board and save for use by generate_baseline.py
for row in range(9):
    for column in range(9):
        _top = row * 88
        _bottom = (row + 1) * 88
        _left = column * 88
        _right = (column + 1) * 88
        square = board.crop((_left, _top, _right, _bottom))
        square.save(f'{row}{column}.png')

print('done')
