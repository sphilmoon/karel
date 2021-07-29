from simpleimage import SimpleImage

def main():
	image = SimpleImage('images/simba-sq.jpg')
	bordered_img = add_border(image, 20)
	bordered_img.show()

def add_border(og_image, border_size):
	"""
	This function returns the original image
	with a black border around it. 
	The border is border_size many pixel thick. 

	Inputs:
		- og_image: the original image to process.
		- border_size: The border thickness to add around the image.

	Returns:
		- A new SimpleImage with the border added around the original image.
	"""
	# border on the both sides, so adding the border size twice.
	new_width = og_image.width + 2*border_size
	new_height = og_image.height + 2*border_size

	# now making the new canvas for the new width and new height.
	bordered_img = SimpleImage.blank(new_width, new_height)

	for x in range(bordered_img.width):
		for y in range(bordered_img.height):
			# setting the border outsie the og image.
			if is_border_pixel(x, y, border_size, bordered_img):
				pixel = bordered_img.get_pixel(x, y)
				pixel.red = 150
				pixel.green = 150
				pixel.blue = 150
			# setting the original image inside the border.
			else:
				og_x = x - border_size
				og_y = y - border_size
				og_pixel = og_image.get_pixel(og_x, og_y)
				bordered_img.set_pixel(x, y, og_pixel)
	return bordered_img

def is_border_pixel(x, y, border_size1, bordered_img):
	"""
	true of false at the pixel (x, y) is the border or not.

	Inputs:
		- x: the x position of the pixel.
		- y: the y position of the pixel.
		- border_size1: the thickness of the border.
		- bordered_img: the bordered image. 
	
	Returns:
		True of false based on the (x, y) pixel is a border pixel. 
	"""
	# left border
	if x < border_size1:
		return True
	# right border
	if x >= bordered_img.width - border_size1:
		return True
	# top border
	if y < border_size1:
		return True
	# bottom border
	if y >= bordered_img.height - border_size1:
		return True
	return False


if __name__ == '__main__':
    main()