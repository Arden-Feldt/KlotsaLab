import gsd.hoomd


class CameraSetter:

    def __init__(self, input_file, output_file):
        self.input_file = "GSDs/" + input_file
        self.output_file = "GSDs/" + output_file

    def set_cam(self):
        """Sets the camera up for the specific simulations, so its centered"""
        print("started setting")

        half_step = 361.8006286621094 / 2

        # Read in the file with the intent to name
        with gsd.hoomd.open(name=self.input_file, mode="r") as file:
            with gsd.hoomd.open(name=self.output_file, mode="w") as modified_file:
                for frame in file:
                    # Get the positions of all particles in the current frame
                    particle_positions = frame.particles.position

                    # Iterate over each particle position
                    for particle_pos in particle_positions:
                        # Update the x and y-coordinates of the particles
                        if particle_pos[0] < 0:
                            particle_pos[0] = (particle_pos[0] + half_step)
                        else:
                            particle_pos[0] = (particle_pos[0] - half_step)

                        if particle_pos[1] <= half_step:
                            particle_pos[1] = (particle_pos[1] + (half_step / 2))
                        else:
                            particle_pos[1] = (particle_pos[1] - (3 / 2 * half_step))

                        if particle_pos[1] >= half_step:
                            particle_pos[1] = particle_pos[1] - (2 * half_step)

                    # Update the positions of particles in the frame
                    frame.particles.position[:] = particle_positions

                    modified_file.append(frame)

        print("finished setting")
