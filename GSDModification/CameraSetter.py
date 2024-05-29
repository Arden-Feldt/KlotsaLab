import gsd.hoomd

class CameraSetter:

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def set_cam(self, x_dim, y_dim, right_shift, up_shift):
        """Sets the camera up for the specific simulations, so its centered"""
        print("started setting")

        # Open the input file for reading
        with gsd.hoomd.open(name=self.input_file, mode="r") as input_file:
            # Open the output file for writing
            with gsd.hoomd.open(name=self.output_file, mode="w") as output_file:
                for frame in input_file:
                    # Get the positions of all particles in the current frame
                    particle_positions = frame.particles.position

                    # Iterate over each particle position
                    for i, particle_pos in enumerate(particle_positions):
                        # Update the x and y-coordinates of the particles
                        particle_pos[0] = (particle_pos[0] + right_shift) % x_dim
                        particle_pos[1] = (particle_pos[1] + up_shift) % y_dim

                        # Ensure the particles are within the bounds
                        if particle_pos[0] < -x_dim / 2:
                            particle_pos[0] += x_dim
                        elif particle_pos[0] > x_dim / 2:
                            particle_pos[0] -= x_dim

                        if particle_pos[1] < -y_dim / 2:
                            particle_pos[1] += y_dim
                        elif particle_pos[1] > y_dim / 2:
                            particle_pos[1] -= y_dim

                        # Update the positions of particles in the frame
                        frame.particles.position[i] = particle_pos

                    # Append the modified frame to the output file
                    output_file.append(frame)

        print("finished setting")



