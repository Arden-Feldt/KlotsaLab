import copy
import os

import gsd.hoomd

import Binner
from ImageReader import ImageReader


def get_final_frame(gsd_file):
    with gsd.hoomd.open(name=gsd_file, mode='r') as file:
        # Get the number of frames
        return len(file)


class Renderer:
    def __init__(self, input_gsd, output_gsd, num_bins, image_path, image_frame):

        self.validate_inputs(input_gsd, output_gsd, num_bins, image_path, image_frame)

        self.input_gsd = input_gsd
        self.output_gsd = output_gsd
        self.num_bins = num_bins
        self.image_path = image_path
        self.image_frame = image_frame

    def gsd_render(self):
        print("started render")

        # Array for particle names
        p_names = {}

        # Read in the file with the intent to name
        with gsd.hoomd.open(name=self.input_gsd, mode="r") as file:

            # Give Each Particle a Name
            for frame_index, frame in enumerate(file):
                if frame_index == self.image_frame:
                    # Locks colors in accordance to image
                    image_reader = ImageReader.ImageReader(self.image_path, self.num_bins)
                    colorlist = image_reader.read()
                    bin_list = image_reader.color_to_binlist(colorlist)
                    image_reader.visualise_colorlist(colorlist)

                    binner = Binner.Binner(frame, self.num_bins, bin_list)
                    p_names = binner.optimize_binning()

            print("started gsd build")

            # Create a new GSD file for writing and set typeid given name
            with gsd.hoomd.open(name=self.output_gsd, mode="w") as modified_file:

                # Looping through and update typeID to reflect name
                for frame_index, frame in enumerate(file):
                    if frame_index <= self.image_frame:
                        # Write the modified frame to the new GSD file
                        modified_file.append(self.id_update(frame, p_names))

        print("finished gsd build")

        print("finished render")

    def id_update(self, frame, p_names):
        """changes id's to names that are passed in"""
        # Make a deep copy of the frame object
        temp_frame = copy.deepcopy(frame)

        for particle_index in range(temp_frame.particles.N):
            # checks there are enough names for the particles
            if temp_frame.particles.N != len(p_names):
                print("Fucked up")
                raise Exception("renderer.id_update(): number of particles and number of names didn't match!")

            # Retrieve the particle name from the dictionary
            particle_name = p_names.get(particle_index)
            if particle_name is not None:
                # Set the typeid for the particle based on the name
                temp_frame.particles.typeid[particle_index] = particle_name

        return temp_frame

    def validate_inputs(self, input_gsd, output_gsd, num_bins, image_path, image_frame):
        if num_bins <= 0:
            raise Exception("Renderer: Num bins must be positive!")
        if image_frame < 0 | image_frame >= get_final_frame(input_gsd):
            raise Exception("Renderer: Final Frame value invalid")

        if self.check_invalid_path(input_gsd):
            raise Exception()
        if self.check_invalid_path(output_gsd):
            raise Exception()
        if self.check_invalid_path(image_path):
            raise Exception()

    def check_invalid_path(self, path):
        if os.path.exists(path):
            if os.path.isfile(path):
                return False
            elif os.path.isdir(path):
                print(f"The path '{path}' is a valid directory.")
            else:
                print(f"The path '{path}' exists but is neither a file nor a directory.")
        else:
            print(f"The path '{path}' does not exist.")

        return True

    # create a binging method
