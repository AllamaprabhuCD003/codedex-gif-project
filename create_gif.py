import imageio.v3 as iio
files=["team-pic1.png","team-pic2.png"]
images=[iio.imread(f"images/{x}") for x in files]
iio.imwrite("team.gif",images,duration=500,loop=0)


# =====GIF Creation Script (Exact 6-line format) =====
# Import imageio.v3 (version 3 of imageio library)
import imageio.v3 as iio
import os

# Set paths
project_folder = '/content/codedex-gif-project'
images_folder = os.path.join(project_folder, 'images')

# Step 1: Define the list of image file names (as per CodeDex tutorial)
filenames = ['team-pic1.png', 'team-pic2.png']

# Step 2: Create an empty list to store image data
images = []

# Step 3: Use a for loop to read images and append to list
for filename in filenames:
    img_path = os.path.join(images_folder, filename)
    images.append(iio.imread(img_path))
    print(f'Loaded: {filename}')

print(f'Total images loaded: {len(images)}')
print()

# Step 4: Create the GIF using iio.imwrite()
output_gif = os.path.join(project_folder, 'team.gif')
iio.imwrite(output_gif, images, duration=500, loop=0)

print('GIF created successfully!')
print(f'Output: {output_gif}')
print('Duration per frame: 500ms')
print('Loop setting: 0 (infinite loop)')
print()
print('GIF Project Complete!')

#Display the generated gif

from IPython.display import Image, display
import os

# Display the generated GIF
gif_path = '/content/codedex-gif-project/team.gif'

print('Generated GIF:')
print(f'Path: {gif_path}')
print(f'File size: {os.path.getsize(gif_path)} bytes')
print()
print('Preview:')
display(Image(gif_path))

# Save the GIF preview as a screenshot
print()
print('GIF preview saved and displayed!')
print()
print('Project Files:')
for root, dirs, files in os.walk('/content/codedex-gif-project'):
    level = root.replace('/content/codedex-gif-project', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in sorted(files):
        file_path = os.path.join(root, file)
        size = os.path.getsize(file_path)
        print(f'{subindent}{file} ({size} bytes)')


