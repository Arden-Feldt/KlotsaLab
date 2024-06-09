import copy
import random

import gsd
import gsd.hoomd
import numpy as np

from GSDModification.ModifierManager import print_columns


class ColorValueWriter:

    def __init__(self, input_gsd, output_gsd):
        self.input_gsd = input_gsd
        self.output_gsd = output_gsd

    def write(self, color_data):
        #  THIS OVERWRITES particle position in the w dim - which is useless for what we are doing, but keep in mind
        print("start color value write")
        with gsd.hoomd.open(name=self.input_gsd, mode="r") as file:

            particle_colors = {}

            # Iterate over each frame in the file
            for frame_index, frame in enumerate(file):
                # Access the particles' orientation property
                orientations = frame.particles.orientation

                # Modify the orientation values as needed
                for particle_index in range(frame.particles.N):
                    # Modify the 'w' component of the orientation quaternion
                    particle_colors[particle_index] = 1

                # Update the orientation property in the frame
                frame.particles.orientation = orientations

            with gsd.hoomd.open(name=self.output_gsd, mode='w') as output_file:
                for frame_index, frame in enumerate(file):
                    # Write the modified frame to the new GSD file
                    output_file.append(self.id_update(frame, particle_colors))

        print("finish color value write")

    def color_update(self, frame, p_names):
        """changes id's to names that are passed in"""
        # Make a deep copy of the frame object
        temp_frame = copy.deepcopy(frame)

        for particle_index in range(temp_frame.particles.N):
            # checks there are enough names for the particles
            if temp_frame.particles.N != len(p_names):
                raise Exception("renderer.id_update(): number of particles and number of names didn't match!")

            # Retrieve the particle name from the dictionary
            particle_name = p_names.get(particle_index)
            if particle_name is not None:
                # Set the typeid for the particle based on the name
                temp_frame.particles.typeid[particle_index] = particle_name

        return temp_frame
