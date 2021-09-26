from simpleimage import SimpleImage

IMAGE_FILENAME = 'simba.jpg'

def inverse(image):
	for pixel in image:

		# loading color components
		red = pixel.red
		green = pixel.green
		blue = pixel.blue

		# inverse color components
		# you gotta substract from 255, the max value.
		inverse_red = 255 - red
		inverse_green = 255 - green
		inverse_blue = 255 - blue

		pixel.red = inverse_red
		pixel.green = inverse_green
		pixel.blue = inverse_blue

	return image

def main():
	# put code here.
	image = SimpleImage(IMAGE_FILENAME)
	image.show()

	inverse = inverse(image)
	inverse.show()

if __name__ == '__main__':
    main()