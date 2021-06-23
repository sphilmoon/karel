from simpleimage import SimpleImage

def darker(image):

	# cutting every pixel in half from its original. 
	for pixel in image:
		pixel.red = pixel.red // 2
		pixel.green = pixel.green // 2
		pixel.blue = pixel.blue // 2

def red_channel(filename):
	image = SimpleImage(filename)
	for pixel in image:
		pixel.green = 0
		pixel.blue = 0
	return image

def compute_luminosity(red, green, blue):
	return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def grayscale(filename):
	image = SimpleImage(filename)
	for pixel in image:
		luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
		pixel.red = luminosity
		pixel.green = luminosity
		pixel.blue = luminosity
	return image

def main():
	flower = SimpleImage('flower.png')
	flower.show()

	darker(flower)
	flower.show()

	red_flower = red_channel('flower.png')
	red_flower.show()

	grayscale_flower = grayscale('flower.png')
	grayscale_flower.show()


if __name__ == '__main__':
    main()