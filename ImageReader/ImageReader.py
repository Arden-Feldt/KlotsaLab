from PIL import Image


def image_reader(path, num_bins):
    """Returns a list of 1s and 0s for pixels in bins depending on if the selected pixel in that bin was black"""

    # Open an image file
    image_path = path
    image = Image.open(image_path)
    result = []

    # get image dimensions and assign bin sizes
    width, height = image.size
    x_bin_size = int(width / num_bins)
    y_bin_size = int(height / num_bins)

    for x in range(0, width, x_bin_size):
        for y in range(0, height, y_bin_size):
            if sum(image.getpixel((x, y))[:3]) < 20:
                result.append(1)
            else:
                result.append(0)

    return result
