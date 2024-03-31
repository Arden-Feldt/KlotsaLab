import gsd.hoomd

if __name__ == '__main__':
    print("started")

    # Array for particle names
    particle_names = {}

    box_dim = 361.8006286621094
    half_step = box_dim / 2

    # Read in the file with the intent to name
    with gsd.hoomd.open(name="modifiable_UNC_gsd.gsd", mode="r") as file:
        with gsd.hoomd.open(name="centered_GSD.gsd", mode="w") as modified_file:
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

            # Update the positions of particles in the frame
                frame.particles.position[:] = particle_positions

                modified_file.append(frame)
