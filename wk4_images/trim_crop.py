from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/simba-sq.png')
    trimmed_img = trim_crop_image(image, 30)

def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_size pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_size is less than half the width of the image.
    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side of the original image

    Returns:
        A new SimpleImage with trim_size pixels shaved off each
        side of the original image
    """

    # TODO: your code here

    #old_image -> crop -> new_image

    #new_image (0,0) = old_image(trim_size,trim_size)
    #new_image(5,0 ) = old_image (trim_size + 5 , trim_size)
    #new_image(10,15) = old_image(trim_size + 10 , trim_size + 15)

    new_width = original_img.width - 2*trim_size
    new_height = original_img.height - 2*trim_size
    new_img = SimpleImage.blank(new_height, new_width)

    for x in range(new_height):
        for y in range(new_width):
            orig_x = x + trim_size
            orig_y = y + trim_size

            orig_pixel = original_img.get_pixel(orig_x,orig_y)
            new_img.set_pixel(x,y,orig_pixel)
        
    return new_img

if __name__ == '__main__':
    main()