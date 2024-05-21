# Arden Feldt's Klotsa Group Work (2023-)
The repository of work I've done as an undergraduate researcher with KlotsaGroup.

## Image Visualizer in Particle Simulations
This is currently the meat of the code in this project. When you run the main, this project paints a image of your choice (like a UNC logo) into a particle simulation (.gsd file). The design comes together at the end, so you get to watch the particles move around until the image forms from the simulation.

## Prerequisites
You need the following to have this work properly
* Hoomd-Blue
  * "HOOMD-blue is a Python package that runs simulations of particle systems on CPUs and GPUs."
  * Ask Daphne Klotsa to provide a tutorial on how to download the package.
  * https://hoomd-blue.readthedocs.io/en/v4.7.0/#
* A .gsd simulation
  * This should also be provided, the .gsd is to big to push to github, but they are on the longleaf cluster.
  * Ideally use one with around 200-500 frames, and a sizable cluster.
  * Put your simulation in GSDs/
* An black and white image
  * I provide two UNC logo options
  * Any black and white .jpeg will work like you want it to.
  * Put them in ImageReader/Images/ (not required)
  
