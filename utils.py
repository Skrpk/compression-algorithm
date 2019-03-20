import numpy as np

def convert_to_brightness_contrast(image):
    image.load()
    height, width = image.size
    converted = []

    for row in range(height):
     for col in range(width):
         pixel = image.getpixel((row,col))
         r, g, b = pixel
         converted_value = 0.3*r + 0.59*g + 0.11*b
         converted.append(converted_value)
    
    return np.asarray(converted)