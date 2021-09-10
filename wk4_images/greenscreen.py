from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.6

# stop.png is my main image
# leaves.png is the background image
# the red part of the main image is replaced by the leaves. 

def main():
	original_stop = SimpleImage('stop.png')
	original_stop.show()

	original_leaves = SimpleImage('leaves.png')
	original_leaves.show()

	stop_is_replaced_by_leaves = redscreen('stop.png', 'leaves.png')
	stop_is_replaced_by_leaves.show()

def redscreen(main_filename, back_filename):
	image = SimpleImage(main_filename)
	back = SimpleImage(back_filename)
	for pixel in image:
		average = (pixel.red + pixel.green + pixel.blue) // 3
		# verifying the pixel is green enough.
		if pixel.red >= average * INTENSITY_THRESHOLD:
			x = pixel.x
			y = pixel.y
			image.set_pixel(x, y, back.get_pixel(x, y)) 
			# overriding x and y with hte background image.
	return image

if __name__ == '__main__':
    main()