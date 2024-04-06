package ImageReader.ImageReader.src;

import java.awt.*;
import java.io.IOException;
import java.util.ArrayList;


public class ImageReader  {

    public ArrayList imageReader(int bins) throws IOException {
        Image image = new PictureImage("i/Users/ethan/feldt_dKlotsa_work/KlotsaPythonCode/pythonProject1/JavaImage/images/halfandhalf.jpeg");

        int h = image.getHeight();
        int w = image.getWidth();

        ArrayList result = new ArrayList<>();

        for (int i = 0; i <= bins * w; i+=w){
            for (int j =0; j <= bins * h; j+=h){
                if (image.getPixelColor(i,j) == Color.black){
                    result.add(1);
                } else {
                    result.add(0);
                }
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        int bins = 10; // Define the number of bins
        ImageReader imageReader = new ImageReader(); // Create an instance of ImageReader

        ArrayList result = imageReader.imageReader(bins);

        // Download the result to your device (for demonstration purposes, just print the result)
        System.out.println("Result: " + result);
    }
}
