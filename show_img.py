#!/usr/bin/env python3

import os
from PIL import Image
from inky.auto import auto
import numpy as np

# Get the current path
PATH = os.path.dirname(__file__)

# Set up the Inky display
try:
    inky_display = auto(ask_user=True, verbose=True)
except TypeError:
    raise TypeError("You need to update the Inky library to >= v1.1.0")

try:
    inky_display.set_border(inky_display.BLACK)
except NotImplementedError:
    pass

img = Image.open(os.path.join(PATH, "goldfinch_800_480.png"))
print(img.size)
img = img.transpose(Image.ROTATE_90)
print(img.size)

#img = img.resize(inky_display.resolution)

inky_display.set_image(img)
inky_display.show()
