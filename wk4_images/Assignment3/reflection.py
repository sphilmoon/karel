"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def main():
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

            # acquiring the top portion.
            new_canvas.set_pixel(x, y, pixel)
            # acquiring the bottom portion.
            new_canvas.set_pixel(x, (height * 2) - (y + 1), pixel)

    return new_canvas

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

if __name__ == '__main__':
    main()