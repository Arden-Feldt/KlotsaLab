def id_update(frame, particle_names):
    """changes id's to names that are passed in"""

    for particle_index in range(frame.particles.N):

        # checks there are enough names for the particles
        if frame.particles.N != len(particle_names):
            print("Fucked up")
            raise Exception("typeID_changer: number of particles and number of names didn't match!")

        # Retrieve the particle name from the dictionary
        particle_name = particle_names.get(particle_index)
        if particle_name is not None:
            # Set the typeid for the particle based on the name
            frame.particles.typeid[particle_index] = particle_name

    return frame