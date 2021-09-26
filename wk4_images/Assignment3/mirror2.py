from simpleimage import SimpleImage

IMAGE_FILENAME = 'simba.jpg'

def main():
	image = SimpleImage(IMAGE_FILENAME)

	# creating an output layout.
	new_canvas = SimpleImage.blank(2 * image.width, image.height)

	for x in range(image.width):
		for y in range(image.height):
			# defining pixels from the OG image.
			pixel = image.get_pixel(x, y) 

			# defining the left side. 
			pixel_left = new_canvas.get_pixel(x, y) 
			# acquire pixel from the OG image.
			pixel_left.red = pixel.red 
			pixel_left.green = pixel.green
			pixel_left.blue = pixel.blue

			# defining the right side. 
			pixel_right = new_canvas.get_pixel(new_canvas.width - 1 - x, y)
			# acquire pixel from the OG image.
			pixel_right.red = pixel.red 
			pixel_right.green = pixel.green
			pixel_right.blue = pixel.blue

if __name__ == '__main__':
    main()