import os

import numpy as np
from PIL import Image

# Take an average of each number to use as our baseline
# https://stackoverflow.com/a/30877800/10696164
for directory in os.listdir('.'):
    # Skip scripts
    if directory.endswith('.py'):
        continue

    # Open all the images for this number
    image_list = [
        Image.open(f'{directory}/{image}') for image in os.listdir(directory)
        if not image.startswith('average')
    ]

    # Create array to store final output
    num_images = len(image_list)
    width, height = image_list[0].size
    array = np.zeros((height, width, 4), dtype=np.float)

    # Build up our output
    avg = image_list[0]
    for i, image in enumerate(image_list[1:]):
        avg = Image.blend(avg, image, 1.0 / float(i + 1))

    avg.save(f'{directory}/average.png')

print('done')
