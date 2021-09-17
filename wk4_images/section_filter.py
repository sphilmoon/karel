from simpleimage import SimpleImage

def main():
	image = SimpleImage('images/simba-sq.jpg')
	image.show()

	for pixel in image:
		average = pixel_average(pixel)

		if average > BRIGHTNESS:
			pixel.red = average
			pixel.green = average
			pixel.blue = average
	
	image.show()

def pixel_average(pixel):
	color_average = (pixel.red + pixel.green + pixel.blue) // 3
	return color_average

	# for px in image: # For-each loop.
	# 	px.red = px.red // 2
	# 	px.green = px.green // 2
	# 	px.blue = px.blue // 2

if __name__ == "__main__":
    main()