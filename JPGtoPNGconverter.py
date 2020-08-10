import sys
import os
from PIL import Image

r"""
Thanks for checking out this JPG to PNG image converter.
This is a simple program created to convert a folder with .JPG
images into a new folder of .PNG images.


To run this converter please enter the following into the terminal:

Example:
    # python3 JPGtoPNGconverter.py (original folder) (new folder)

For this specific set of files used in this project:
    # python3 JPGtoPNGconverter.py Pokedex\ new\

"""

# Grab the first and second argument
img_folder = sys.argv[1]
output_folder = sys.argv[2]

# Check if new\ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through Pokedex, convert images to PNG
# Save to the new folder.
img_num = 1
for file in os.listdir(img_folder):
    img = Image.open(f'{img_folder}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print(f'Image {img_num} converted successfully.')
    img_num += 1
