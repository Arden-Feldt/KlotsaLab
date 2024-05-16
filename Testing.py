import Renderer

box_dim = 361.8006286621094

# Where you pass in all relevant information to create the visual
if __name__ == '__main__':
    renderer = Renderer.Renderer("GSDs/modifiable_UNC_gsd.gsd",
                                 "GSDs/clone_of_modifile.gsd",
                                 4,
                                 "/Users/ethan/feldt_dKlotsa_work/KlotsaPythonCode"
                                 "/pythonProject1/ImageReader/Images/UNCLogo.jpeg")

    renderer.gsd_render()
