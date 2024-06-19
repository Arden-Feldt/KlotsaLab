from PIL import Image


class ImageReader:

    def __init__(self, path, num_bins):
        self.path = path
        self.num_bins = num_bins

    def read_grayscale(self):
        """Returns a list of values in [0, 1] for pixels in bins corresponding with if pixel in that bin was black"""

        print("started reading")

        # Open an image file
        image_path = self.path
        image = Image.open(image_path).convert('L')  # Convert image to grayscale

        result = []

        # get image dimensions and assign bin sizes
        width, height = image.size

        print("image width: ", width, "\nimage height: ", height)

        x_bin_size = int(width / self.num_bins)
        y_bin_size = int(height / self.num_bins)

        for x in range(0, width, x_bin_size):
            for y in range(0, height, y_bin_size):
                pixel_value = image.getpixel((x, y))
                normalized_value = pixel_value  # / 255 # Normalize pixel value to range [0, 1]
                result.append(normalized_value)

        print("finished reading")

        return result

    def read_black_and_white(self):
        """Returns a list of 1s and 0s for pixels in bins depending on if the selected pixel in that bin was black"""

        print("started reading")

        # Open an image file
        image_path = self.path
        image = Image.open(image_path).convert('1')
        result = []

        # get image dimensions and assign bin sizes
        width, height = image.size

        print("image width: ", width, "\nimage height: ", height)

        x_bin_size = int(width / self.num_bins)
        y_bin_size = int(height / self.num_bins)

        for x in range(0, width, x_bin_size):
            for y in range(0, height, y_bin_size):
                if sum(image.getpixel((x, y))[:3]) < 20:
                    result.append(1)
                else:
                    result.append(0)

        print("finished reading")

        return result

    def color_to_binlist(self, color_list):
        print("started binlisting")

        binlist = set()
        for i in range(0, len(color_list)):
            if color_list[i] == 1:
                binlist.add(i)

        print("finished binlisting")
        return binlist

    def visualise_colorlist(self, colorlist):
        i = 0
        for bin_color in colorlist:
            print(bin_color, end=' ')
            i += 1
            if i % self.num_bins == 0:
                print("")

    from PIL import Image

    def read_color(self):
        """Returns three lists of values in [0, 255] for pixel color in bins corresponding with that pixel"""

        print("started reading")

        # Open an image file
        image_path = self.path
        image = Image.open(image_path).convert('RGB')  # Convert image to RGB

        # Initialize lists for each color channel
        red_values = []
        green_values = []
        blue_values = []

        # Get image dimensions and assign bin sizes
        width, height = image.size

        print("image width: ", width, "\nimage height: ", height)

        x_bin_size = int(width / self.num_bins)
        y_bin_size = int(height / self.num_bins)

        for x in range(0, width, x_bin_size):
            for y in range(0, height, y_bin_size):
                r, g, b = image.getpixel((x, y))
                red_values.append(r)
                green_values.append(g)
                blue_values.append(b)

        return red_values, green_values, blue_values
