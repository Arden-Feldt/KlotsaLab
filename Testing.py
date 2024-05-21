import Renderer
from GSDModification.ModifierManager import set_camera, copy_gsd, check_write

box_dim = 361.8006286621094

# Where you pass in all relevant information to create the visual
if __name__ == '__main__':

    # function used to copy a gsd to a new file
    # copy_gsd("modifiable_UNC_gsd.gsd", "centered_gsd.gsd")

    # TODO: make this more general
    # sets the camera to a specific location, only useful if you have my gsd.
    # set_camera("modifiable_UNC_gsd.gsd", "centered_gsd.gsd")

    # check if you can write to a specific gsd
    # check_write("clone_of_modifile.gsd")

    # num_bins must be a factor of image height and size
    # TODO: Make colorlist -> bins a hashset
    renderer = Renderer.Renderer("centered_gsd.gsd",
                                 "clone_of_modifile.gsd",
                                 600,
                                 "/Users/ethan/feldt_dKlotsa_work/KlotsaPythonCode"
                                 "/pythonProject1/ImageReader/Images/clusterUNC.jpeg")

    renderer.gsd_render()

    # TODO: Add post proc
    # TODO: Add color

