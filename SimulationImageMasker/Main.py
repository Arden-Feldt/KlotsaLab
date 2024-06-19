import GrayscaleRenderer
from GSDModification.ModifierManager import get_final_frame, copy_gsd, set_camera, check_write

# Where you pass in all relevant information to create the visual
if __name__ == '__main__':

    # UTILITY FUNCTIONS:
    # copy_gsd("GSDs/clone_of_modifile.gsd" , "GSDs/sifted.gsd" )
    # set_camera(<input gsd>, <output gsd>, <right shift>, <up_shift>)
    # check_write(<gsd with unclear permissions>)

    input_gsd = "GSDs/centered_gsd.gsd"                             # the gsd you'll read in and copy
    output_gsd = "GSDs/clone_of_modifile.gsd"                       # the gsd the program will make, update, and save
    num_bins = 640                                                  # the # of bins on an axis, total bins = num_bins^2
    image_path = "SimulationImageMasker/ImageReader/Images/klotsa_daphne.jpeg"  # Path to black & white image you're using
    image_frame = get_final_frame(input_gsd) - 1                    # Frame where the image comes together

    renderer = GrayscaleRenderer.GrayscaleRenderer(input_gsd,
                                 output_gsd,
                                 num_bins,
                                 image_path,
                                 image_frame)

    renderer.gsd_render()

    # TODO: put a thin boundry around particles

    # TODO: alternativly loop through particles
    # TODO: implement with color coding in Ovito

    # TODO: read general info/grants/crowdspecific/ UNC SEED
    # TODO: app applications
        # Running trails
        # bluetooth finder
        # walking traffic in a city
        # not lose your running group sataliet

