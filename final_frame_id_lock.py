import numpy as np

particle_names = {}


def particle_namer(frame):
    # Splits the simulation down the middle by the last frame
    for particle_idx in range(frame.particles.N):
        particle_position = frame.particles.position[particle_idx]
        # Generate particle name based on the condition
        particle_name = 1 if particle_position[0] >= 0 else 0
        # Store the particle name in the dictionary
        particle_names[particle_idx] = particle_name
    return particle_names

#create a binging method
def binning_method(frame, num_bins, box_dim, highlight_bin_list):
    for particle_idx in range(frame.particles.N):
        particle_position = frame.particles.position[particle_idx]

        current_bin = 0;

        for x in np.arange(-box_dim/2, box_dim/2, box_dim / num_bins):
            for y in np.arange(-box_dim/2, box_dim/2, box_dim / num_bins):
                # check to see if particle is in current bin
                if x <= particle_position[0] < x + box_dim / num_bins and y <= \
                        particle_position[1] < y + box_dim / num_bins:
                    # name particle given on if bin is in binlist
                    particle_name = 1 if current_bin in highlight_bin_list else 0
                    # Store the particle name in the dictionary
                    particle_names[particle_idx] = particle_name
                current_bin += 1
                y += box_dim / num_bins
            x += box_dim / num_bins
    return particle_names

def create_bin_list(num_bins):
    result = []
    flipper = 0
    for bin in np.arange(0, num_bins ** 2, 1):
        if (bin + flipper) % 2 == 0:
            result.append(bin)
        if bin % 16 == 0:
            flipper += 1
    return result

