from PIL import Image
import numpy as np
from utils import convert_to_brightness_contrast

SQUARE_EDGE_SIZE = 4

def run():
    image = Image.open('images/nature.bmp')

    coef_array = convert_to_brightness_contrast(image)
    compressed_array = []
    height, width = image.size

    for row in range(int(height / SQUARE_EDGE_SIZE)):
     for col in range(int(width / SQUARE_EDGE_SIZE)):
         pixel = image.getpixel((row * SQUARE_EDGE_SIZE + 1, col * SQUARE_EDGE_SIZE + 1))
         r, g, b = pixel
         converted_value = 0.3*r + 0.59*g + 0.11*b
         compressed_array.append(converted_value)

    return compressed_array

run()