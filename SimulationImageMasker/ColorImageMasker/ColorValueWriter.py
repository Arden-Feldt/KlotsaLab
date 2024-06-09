import gsd
import gsd.hoomd
import numpy as np

from GSDModification.ModifierManager import print_columns


class ColorValueWriter:

    def __init__(self, input_gsd, output_gsd):
        self.input_gsd = input_gsd
        self.output_gsd = output_gsd

    def write(self):
        print("start color value write")

        # Open the input GSD file
        with gsd.hoomd.open(name=self.input_gsd, mode='r') as input_file:
            frames = [frame for frame in input_file]

        # Modify the frames
        for frame in frames:
            self.add_custom_property(frame)

        # Write the modified frames to a new GSD file
        with gsd.hoomd.open(name=self.output_gsd, mode='w') as output_file:
            for frame in frames:
                output_file.append(frame)

        print("finish color value write")
