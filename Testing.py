import Renderer

box_dim = 361.8006286621094

# Where you pass in all relevant information to create the visual
if __name__ == '__main__':
    # num_bins must be a factor of image height and size
    # TODO: Optimize for loops
    # TODO: Make colorlist -> bins a hashset
    renderer = Renderer.Renderer("centered_gsd.gsd",
                                 "clone_of_modifile.gsd",
                                 10,
                                 "/Users/ethan/feldt_dKlotsa_work/KlotsaPythonCode"
                                 "/pythonProject1/ImageReader/Images/UNCLogo.jpeg")

    # TODO: Add color
    renderer.gsd_render()
