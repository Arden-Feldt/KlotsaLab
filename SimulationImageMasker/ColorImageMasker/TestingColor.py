import gsd.hoomd
import numpy as np

# just here so I can figure out what does/doesn't work before I implement it where it belongs


# update: this is garbage
class TestingColor:

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

        self.print_columns(self.output_gsd)

        print("finish color value write")

    def add_custom_property(self, frame):
        n = frame.particles.N
        custom_property = np.random.rand(n).astype(np.float32)  # Generate some random data for the custom property

        # Check if 'custom' exists in the frame
        if hasattr(frame.particles, 'custom'):
            print("dude its there")
        else:
            # Initialize 'custom' if it doesn't exist
            frame.create("custom", data_type='float', components=1)

        # Add the custom property
        frame.particles.custom[...] = custom_property
        print("Added custom property.")

    def print_columns(self, gsd_file):
        # Open the GSD file in read mode
        with gsd.hoomd.open(name=gsd_file, mode='rb') as file:
            for frame_index, frame in enumerate(file):
                print(f"Frame {frame_index + 1}")

                # Print out the number of particles
                num_particles = frame.particles.N
                print(f"Number of particles: {num_particles}")

                # Print out particle positions
                if frame.particles.position is not None:
                    print("Positions")
                    print("example: ", frame.particles.position[0])

                # Print out particle velocities
                if frame.particles.velocity is not None:
                    print("Velocities")
                    print("example: ", frame.particles.velocity[0])

                # Print out particle typeids
                if frame.particles.typeid is not None:
                    print("Type IDs")
                    print("example: ", frame.particles.typeid[0])

                # Print out custom properties if they exist
                if 'custom' in frame.particles.data:
                    print("Custom Properties (e.g., 'custom_property'):")
                    print("example: ", frame.particles.data['custom']['custom_property'][0])

                print("-" * 40)


input_gsd = "/Users/ethan/feldt_dKlotsa_work/KlotsaPythonCode/pythonProject1/GSDs/clone_of_modifile.gsd"
output_gsd = "/Users/ethan/feldt_dKlotsa_work/KlotsaPythonCode/pythonProject1/GSDs/colorvalgsd.gsd"
writer = TestingColor(input_gsd, output_gsd)
writer.write()
