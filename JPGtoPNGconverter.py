import sys
import os
from PIL import Image

# Grab the first and second argument
img_folder = sys.argv[1]
output_folder = sys.argv[2]

# print('Number of arguments: ', len(sys.argv))
# print('Argument 0 is: ', str(sys.argv[0]))
# print('Argument 1 is: ', sys.argv[1])
# print('Argument 2 is: ', sys.argv[2])

# Check if new\ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through Pokedex, convert images to PNG
# Save to the new folder.
for file in os.listdir(img_folder):
    img = Image.open(f'{img_folder}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('Image Converted')



