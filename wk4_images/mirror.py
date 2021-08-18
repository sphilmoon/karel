from simpleimage import SimpleImage

def main():
	original = SimpleImage('burrito.jpg')
	original.show()

	mirrored = mirror_image('burrito.jpg')
	mirrored.show()


def mirror_image(filename):
	image = SimpleImage(filename)
	width = image.width
	height = image.height

	# creating a canvas for the new image.
	mirror = SimpleImage.blank(width * 2, height)

	for y in range(height):
		for x in range(width): # inner loop always completes first. 
			pixel = image.get_pixel(x, y) # defining the original image
			mirror.set_pixel(x, y, pixel) # for the left-hand half
			# for the right-hand half in backward
			mirror.set_pixel((width * 2) - (x + 1), y, pixel) 
	return mirror

if __name__ == '__main__':
    main()