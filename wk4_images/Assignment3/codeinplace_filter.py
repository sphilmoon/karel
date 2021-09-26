"""
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    # TODO: your code here
    # rad_stanford = rad_channel(image)

    # Show the image after the transform
    rad_picture = rad_channel(DEFAULT_FILE)
    rad_picture.show()

def rad_channel(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red * 1.5
        pixel.green = pixel.green * 0.7
        pixel.blue = pixel.blue *1.5
    return image

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()