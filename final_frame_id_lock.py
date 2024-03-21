particle_names = {}


def particle_namer(frame):
    for particle_idx in range(frame.particles.N):
        particle_position = frame.particles.position[particle_idx]
        # Generate particle name based on the condition
        particle_name = 1 if particle_position[0] >= 0 else 0
        # Store the particle name in the dictionary
        particle_names[particle_idx] = particle_name
    return particle_names
