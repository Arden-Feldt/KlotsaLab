import gsd.hoomd

import Binner
from ImageReader import ImageReader


class Renderer:
    def __init__(self, input_gsd, output_gsd, num_bins, image_path):
        self.input_gsd = input_gsd
        self.output_gsd = output_gsd
        self.num_bins = num_bins
        self.image_path = image_path

    def gsd_render(self):
        print("started")

        # Array for particle names
        p_names = {}

        # Read in the file with the intent to name
        with gsd.hoomd.open(name=self.input_gsd, mode="r") as file:

            # Give Each Particle a Name
            for frame_index, frame in enumerate(file):
                if frame_index == 349:
                    # Locks colors in accordance to image
                    colorlist = ImageReader.image_reader(self.image_path, self.num_bins)
                    bin_list = ImageReader.color_to_binlist(colorlist)

                    binner = Binner.Binner(frame, self.num_bins, bin_list)

                    p_names = binner.binning_method()

            # Create a new GSD file for writing and set typeid given name
            with gsd.hoomd.open(name=self.output_gsd, mode="w") as modified_file:

                # Looping through and update typeID to reflect name
                for frame_index, frame in enumerate(file):
                    # Write the modified frame to the new GSD file
                    modified_file.append(self.id_update(frame, p_names))

        print("finished")

    def id_update(self, frame, p_names):
        """changes id's to names that are passed in"""

        for particle_index in range(frame.particles.N):

            # checks there are enough names for the particles
            if frame.particles.N != len(p_names):
                print("Fucked up")
                raise Exception("typeID_changer: number of particles and number of names didn't match!")

            # Retrieve the particle name from the dictionary
            particle_name = p_names.get(particle_index)
            if particle_name is not None:
                # Set the typeid for the particle based on the name
                frame.particles.typeid[particle_index] = particle_name

        return frame

    def particle_namer(self, frame):
        """Splits the simulation down the middle - used for testing"""
        # Splits the simulation down the middle by the last frame
        for particle_idx in range(frame.particles.N):
            particle_position = frame.particles.position[particle_idx]
            # Generate particle name based on the condition
            particle_name = 1 if particle_position[0] >= 0 else 0
            # Store the particle name in the dictionary
            particle_names[particle_idx] = particle_name
        return particle_names

    # create a binging method
