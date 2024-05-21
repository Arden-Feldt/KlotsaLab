# Arden Feldt's Klotsa Lab Work (2023-)
The repository of work I've done as an undergraduate researcher with Klotsa Group.

## Image Visualizer in Particle Simulations
This is currently the meat of the code in this project. When you run the main, this project paints a image of your choice (like a UNC logo) into a particle simulation (.gsd file). The design comes together at the end, so you get to watch the particles move around until the image forms from the simulation.

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

### Main
Once you're happy with the parameters you pass into Renderer(), just run everything from here. Additionally there are three commented out utility functions that can be very useful, more on those later. The process should finish well within five minutes, if it doesn't something is wrong.

### Renderer
This class does most of the heavy lifting. It'll call other functions to read in your selected image (ImageReader.py), bin up your simulation, and then assign particle id's to each bin per the selected image(Binner.py). Then it'll build the new .gsd, this should take the longest, about 2 minutes.

### Binner
optimize_binning() will cut up your simulation into little pixel like boxes, and then does the actual id setting.

### ImageReader
Reads in a black and white .jpeg and returns an array that will line up with the simulation bins. The image will only care about the parts of the image that are black, marking them as 1 and everything else a 0. Also other image types don't seem to work for the most part, but you can mess with that.

### GSDModification
Inside this directory are three files that each provide small utility tasks that were helpful to me while I was at the lab.

#### GSDCopier.py
Takes in an input .gsd and copies it frame by frame to the output .gsd. Useful for when you corrupt or mangle a file. Always have a backup of whatever simulation you are working on saves somewhere far away from your program.
#### RWgsdChecker.py
Checks if you can write to a specific .gsd. This should always return true, but its useful in niche troubleshooting situations.
#### CameraSetter.py
Sets the camera to a new position. If I'm being honest, unless you have my simulation, you're probably going to have to rewrite the math here so it works for wherever your cluster is.
