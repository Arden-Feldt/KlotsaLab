import gsd
import gsd.hoomd
import numpy as np


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

        def add_custom_property(frame):
            n = frame.particles.N
            custom_property = np.random.rand(n).astype(np.float32)  # Generate some random data for the custom property

            # Check if the frame already has 'custom_property'
            if hasattr(frame.particles, 'custom_property'):
                print("Custom property already exists. Overwriting.")
            else:
                print("Adding custom property.")

            # Assign the custom property to the particles
            frame.particles.custom_property = custom_property
