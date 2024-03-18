import gsd.hoomd

if __name__ == '__main__':
    print("started")

    # Array for particle names
    particle_names = {}

    # Read in the file with the intent to name
    with gsd.hoomd.open(name="modifiable_UNC_gsd.gsd", mode="r") as file:
        # Iterate over each frame in the original file
        for frame_index, frame in enumerate(file):
            if frame_index == 349:
                for particle_idx in range(frame.particles.N):
                    particle_position = frame.particles.position[particle_idx]
                    # Generate particle name based on the condition
                    particle_name = 1 if particle_position[0] >= 0 else 0
                    # Store the particle name in the dictionary
                    particle_names[particle_idx] = particle_name

        # Create a new GSD file for writing and set typeid given name
        with gsd.hoomd.open(name="clone_of_modifile.gsd", mode="w") as modified_file:
            # Write all subsequent frames to the new GSD file
            for frame_index, frame in enumerate(file):
                # Iterate over each particle in the frame
                for particle_index in range(frame.particles.N):
                    # Retrieve the particle name from the dictionary
                    particle_name = particle_names.get(particle_index)
                    if particle_name is not None:
                        # Set the typeid for the particle based on the name
                        frame.particles.typeid[particle_index] = particle_name

                # Write the modified frame to the new GSD file
                modified_file.append(frame)
    print(particle_names)
    print("finished")