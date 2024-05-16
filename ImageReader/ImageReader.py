from PIL import Image


def color_to_binlist(color_list):
    binlist = []
    for i in range(0, len(color_list)):
        if color_list[i] == 1:
            binlist.append(i)
    return binlist


class ImageReader:

    def __init__(self, path, num_bins):
        self.path = path
        self.num_bins = num_bins

    def read(self):
        """Returns a list of 1s and 0s for pixels in bins depending on if the selected pixel in that bin was black"""

        # Open an image file
        image_path = self.path
        image = Image.open(image_path)
        result = []

        # get image dimensions and assign bin sizes
        width, height = image.size
        x_bin_size = int(width / self.num_bins)
        y_bin_size = int(height / self.num_bins)

        for x in range(0, width, x_bin_size):
            for y in range(0, height, y_bin_size):
                if sum(image.getpixel((x, y))[:3]) < 20:
                    result.append(1)
                else:
                    result.append(0)
        return result
