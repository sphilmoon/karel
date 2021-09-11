from simpleimage import SimpleImage

def main():
	image = SimpleImage('images/karel.png')
	trimmed_img = trim_crop_image(image, 30)
	trimmed_img.show()

def trim_crop_image(og_image, trim_size):
	"""
	This function crop each side (top, bottom, left, right) of the og image.
	trim_size is the thickness of the cropping at pixel level.

	Inputs:
		- og_image: the original image to process.
		- trim_size: the crop thickness of each side.  

	Returns:
		- A new SimpleImage with the cropped size of the og image. 
	"""
	# crop on the both sides, so removing twice on each side. 
	new_width = og_image.width - (2*trim_size)
	new_height = og_image.height - (2*trim_size)

	# now making a new canvas to add the cropped image. 
	trimmed_image = SimpleImage.blank(new_width, new_height)

	for x in range(new_width):
		for y in range(new_height):
			og_x = x + trim_size
			og_y = y + trim_size
			og_pixel = og_image.get_pixel(og_x, og_y)
			trimmed_image.set_pixel(x, y, og_pixel)
	return trimmed_image


if __name__ == '__main__':
    main()