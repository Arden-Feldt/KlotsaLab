import gsd.hoomd

if __name__ == '__main__':
    print("started")

    # Array for particle names
    particle_names = {}
    box_dim = 361.8006286621094
    half_step = box_dim / 2

    # Read in the file with the intent to name
    with gsd.hoomd.open(name="modifiable_UNC_gsd.gsd", mode="r") as file:

        for frame in file:
            # Get the positions of all particles in the current frame
            particle_positions = frame.particles.position

            # Iterate over each particle position
            for particle_pos in particle_positions:
                # Update the x-coordinate of the particle
                if particle_pos[0] <= 0:
                    particle_pos[0] = (particle_pos[0] + half_step)
                if particle_pos[0] > 0:
                    particle_pos[0] = ((particle_pos[0] + half_step) % box_dim) - half_step

            # Update the positions of particles in the frame
            frame.particles.position[:] = particle_positions

        # Create a new GSD file for writing and set typeid given name
        with gsd.hoomd.open(name="centered_GSD", mode="w") as modified_file:
            modified_file.append(frame)
