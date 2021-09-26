"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def main():
	# Let's decompose.
    # Get file name from user input
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Show the reflected image
    reflected = make_reflected(filename)
    reflected.show()

def make_reflected(filename):
    image = SimpleImage(filename)
    height = image.height
    width = image.width
    # TODO: your code here.
    # creating an output layout.

    new_canvas = SimpleImage.blank(width, 2 * height)

    for y in range(height):
        for x in range(width):
            # defining and acquiring the OG image. 
            pixel = image.get_pixel(x, y)
            # defining and acquiring the top portion.
            pixel_top = new_canvas.get_pixel(x, y)
			# overlaying from the OG image.
			pixel_top.red = pixel.red
			pixel_top.green = pixel.green
			pixel_top.blue = pixel.blue
            # defining and acquiring the bottom portion.
			pixel_bottom = new_canvas.get_pixel(x, (height * 2) - (y + 1))
			# overlaying from the OG image.
			pixel_bottom.red = pixel.red
			pixel_bottom.green = pixel.green
			pixel_bottom.blue = pixel.blue

    return new_canvas

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()