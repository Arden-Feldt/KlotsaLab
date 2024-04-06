package ImageReader.ImageReader.src;

import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;

public class PictureImage implements Image {
    private final BufferedImage image;

    public PictureImage(String pathname) throws IOException {
        this.image = ImageIO.read(new File(pathname));
    }

    @Override
    public Color getPixelColor(int x, int y) {
        return new Color(image.getRGB(x, y));
    }

    @Override
    public int getWidth() {
        return image.getWidth();
    }

    @Override
    public int getHeight() {
        return image.getHeight();
    }

    @Override
    public int getNumLayers() {
        return 1;
    }
}