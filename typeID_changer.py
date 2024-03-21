def id_update(frame, particle_names):
    for particle_index in range(frame.particles.N):
        # Retrieve the particle name from the dictionary
        particle_name = particle_names.get(particle_index)
        if particle_name is not None:
            # Set the typeid for the particle based on the name
            frame.particles.typeid[particle_index] = particle_name

    return frame