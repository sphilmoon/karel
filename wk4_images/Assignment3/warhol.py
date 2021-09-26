"""
Pseudocode / roadmap / decompose:

Creating a 2 x 3, total 6 patches of images on a new canvas. 

# 1: make_recolored_patch(red_scale, green_scale, blue_scale)

# 2: make_new_canvas

# 3: put_patch_on_new_canvas(final_image, start_x, start_y, patch)

# 4: Add to the top row.

# 5: Add to the bottom row. 
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE # for the new canvas.
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
	# creating a new canvas.
	final_image = SimpleImage.blank(WIDTH, HEIGHT)
	final_patching(final_image)
	final_image.show()

	# pink_patch = make_recolored_patch(1.5, 0, 1.5) # pinkish patch.
	# pink_patch.show()

	# put_patch = put_patch_on_new_canvas(final_image, 2, 0, pink_patch)
	# put_patch.show()

	# final_image.show()

def random_patches():
	red = random.uniform(-0.5, 2.5)
	green = random.uniform(-0.5, 2.5)
	blue = random.uniform(-0.5, 2.5)
	return red, green, blue

def make_recolored_patch(red_scale, green_scale, blue_scale):
	patch = SimpleImage(PATCH_NAME)
	for pixel in patch:
		pixel.red *= red_scale
		pixel.green *= green_scale
		pixel.blue *= blue_scale
	return patch

def put_patches_on_new_canvas(final_image, column, row, pink_patch):
	for y in range(PATCH_SIZE):
		for x in range(PATCH_SIZE):
			pixel = pink_patch.get_pixel(x, y)
			final_image.set_pixel(x + (column*PATCH_SIZE), y + (row*PATCH_SIZE), pixel)
	return final_image

def final_patching(final_image):
	for y in range(N_ROWS):
		for x in range(N_COLS):
			red, green, blue = random_patches()
			pink_patch = make_recolored_patch(red, green, blue)
			put_patches_on_new_canvas(final_image, x, y, pink_patch)


if __name__ == '__main__':
    main()