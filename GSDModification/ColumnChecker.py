import gsd
import gsd.hoomd


class ColumnChecker:

    def __init__(self, gsd_file_path):
        self.gsd_file_path = gsd_file_path

    def print_columns(self):
        # Open the GSD file in read mode
        with gsd.hoomd.open(name=self.gsd_file_path, mode='r') as file:
            # Read the first frame
            frame_index, frame = next(enumerate(file))

            print("-" * 40)
            print(f"Column Checker, Frame {frame_index + 1}")

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
            if hasattr(frame.particles, 'custom'):
                print("Custom Properties (e.g., 'custom'):")
                print("example: ", frame.particles.custom[0])

            print("-" * 40)
