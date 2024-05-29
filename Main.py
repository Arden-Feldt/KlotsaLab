import Renderer
from GSDModification.ModifierManager import set_camera, copy_gsd, check_write, get_x_box_dim, get_y_box_dim, \
    get_final_frame

# Where you pass in all relevant information to create the visual
if __name__ == '__main__':

    # UTILITY FUNCTIONS:
    # copy_gsd(<your gsd>, <new gsd>)
    # set_camera(<input gsd>, <output gsd>, <right shift>, <up_shift>)
    # check_write(<gsd with unclear permissions>)

    input_gsd = "GSDs/centered_gsd.gsd"                              # the gsd you'll read in and copy
    output_gsd = "GSDs/clone_of_modifile.gsd"                        # the gsd the program will make, update, and save
    num_bins = 600                                                   # the # of bins on an axis, total bins = num_bins^2
    image_path = "ImageReader/Images/clusterUNC.jpeg"                # Path to black and white image you're using
    image_frame = get_final_frame(input_gsd) - 1            # Frame where the image comes together

    # num_bins must be a factor of image height and size
    renderer = Renderer.Renderer(input_gsd,
                                 output_gsd,
                                 num_bins,
                                 image_path,
                                 image_frame)

    renderer.gsd_render()

