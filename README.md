# Arden Feldt's Klotsa Lab Work (2023-)
The repository of work I've done as an undergraduate researcher with Klotsa Group.

## Image Visualizer in Particle Simulations
This is currently the meat of the code in this project. When you run the main, this project paints a image of your choice (like a UNC logo) into a particle simulation (.gsd file). The design comes together at the end (or a frame of your choice), so you get to watch the particles move around until the image forms from the simulation. You can see what this looks like by downloading lowresFinalVisual.mp4. I've made a lot of changes to make sure its a generalized and friendly as possible, but if you stray to far from what I was originally doing you may have to patch up some edge cases. I've cleaned up every one I found while I worked at the lab.

## Prerequisites
You need the following to have this work properly
* Hoomd-Blue
  * "HOOMD-blue is a Python package that runs simulations of particle systems on CPUs and GPUs."
  * Ask Daphne Klotsa to provide a tutorial on how to download the package.
  * Nick Lauersdorf repo with tutorial: https://github.com/njlauersdorf/ABPs/tree/master 
  * https://hoomd-blue.readthedocs.io/en/v4.7.0/#
* A .gsd simulation
  * This should also be provided, the .gsd is to big to push to github, but they are on the longleaf cluster.
  * Ideally use one with around 200-500 frames, and a sizable cluster.
  * Put your simulation in GSDs/
* An black and white image
  * I provide two UNC logo options
  * Any black and white .jpeg will work like you want it to.
  * Put them in ImageReader/Images/ (not required)

## Class Descriptors

### Main.py
Once you're happy with the parameters you pass into Renderer(), just run everything from here. Additionally there are three commented out utility functions that can be very useful, more on those later. The process should finish well within five minutes, if it doesn't something is wrong.

### Renderer.py
This class does most of the heavy lifting. It'll call other functions to read in your selected image (ImageReader.py), bin up your simulation, and then assign particle id's to each bin per the selected image(Binner.py). Then it'll build the new .gsd, this should take the longest of any part of the rendering process, about 2 minutes.

#### Renderer takes in the following parameters, and its crucial you understand them.
* input_gsd
  * This is the gsd you are going to read in.
  * This should be provided by Dr. Klotsa or Nick.
  * This file will not, and should not, be modified in any way.
* output_gsd
  * This is the path and name where the programs output will end up.
  * Make sure you specify it's a .gsd.
* num_bins
  * This is the number of bins on each axis.
  * The total number of bins will be num_bins^2
  * This number MUST be a factor of the dimensions of your image. Its recommended to make your image a square and set num_bins to the number of pixels on each side.
* image_path
  * This is just the path to the black and white .jpeg you selected.
  * It's easiest if this image is a square, as the simulation will then paint one-to-one on the simulation.
* image_frame
  * This is the frame of your simulation where the image comes together.
  * Setting image_frame to **get_final_frame(input_gsd) - 1** will make the image come together at the last frame of the simulation.
  * The image_frame must be a number less then the number of frames in your simulation.

### Binner.py
optimize_binning() will cut up your simulation into little pixel like boxes and save for each particle if they are inside the image mask or not, but Renderer.id_update() then does the actual particle id setting.

### ImageReader.py
Reads in a black and white .jpeg and returns an array that will line up with the simulation bins. The image will only care about the parts of the image that are black, marking them as 1 and everything else a 0. Also other image types don't seem to work for the most part, but you can mess with that.

### GSDModification
Inside this directory are three files that each provide small utility tasks that were helpful to me while I was at the lab. These can often take a while so let them chug. There are also some utility functions in here, like get_x_box_dim() and get_y_box_dim().

#### GSDCopier.py
Takes in an input .gsd and copies it frame by frame to the output .gsd. Useful for when you corrupt or mangle a file. Always have a backup of whatever simulation you are working on saves somewhere far away from your program.

#### RWgsdChecker.py
Checks if you can write to a specific .gsd. This should always return true, but its useful in niche troubleshooting situations.

#### CameraSetter.py
Often the cluster formed in these simulations are not in the middle of the frame. This function lets you specify a shift right and up, so you can center the cluster. Each simulation will need a different offset. Particles pushed outside of the enviornment wrap around the other side. To properly specify the offset you must know the box dimensions of your simulation, which you can see with get_x_box_dim() and get_y_box_dim(). The dimensions should be the same (to my knowledge), but just in case they are not my code takes that into account. For example my box dimensions were around 361.
## 
*1000001 01000110*
