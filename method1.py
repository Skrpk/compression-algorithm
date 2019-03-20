from PIL import Image
import numpy as np
from utils import convert_to_brightness_contrast

def run():
    image = Image.open('images/nature.bmp')

    newImage = image.resize((160, 120))
    newImage.save('images/nature_resized.bmp')

run()