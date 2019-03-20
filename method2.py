from PIL import Image
import numpy as np

SQUARE_EDGE_SIZE = 4

def run():
    image = Image.open('images/nature.bmp')

    compressed_array = []
    height, width = image.size

    for row in range(int(height / SQUARE_EDGE_SIZE)):
     for col in range(int(width / SQUARE_EDGE_SIZE)):
         pixel = image.getpixel((row * SQUARE_EDGE_SIZE, col * SQUARE_EDGE_SIZE))
         r, g, b = pixel
         converted_value = 0.3*r + 0.59*g + 0.11*b
         compressed_array.append(converted_value)

    return compressed_array

run()