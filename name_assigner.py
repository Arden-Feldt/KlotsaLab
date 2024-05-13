import numpy as np

import ImageReader.ImageReader

particle_names = {}


def particle_namer(frame):
    """Splits the simulation down the middle - used for testing"""
    # Splits the simulation down the middle by the last frame
    for particle_idx in range(frame.particles.N):
        particle_position = frame.particles.position[particle_idx]
        # Generate particle name based on the condition
        particle_name = 1 if particle_position[0] >= 0 else 0
        # Store the particle name in the dictionary
        particle_names[particle_idx] = particle_name
    return particle_names


# create a binging method
def binning_method(frame, num_bins, box_dim, highlight_bin_list):
    """Used to create comple images in simulation by cutting it into managable bins - assigns names"""
    for particle_idx in range(frame.particles.N):
        particle_position = frame.particles.position[particle_idx]

        current_bin = 0;

        for x in np.arange(-box_dim / 2, box_dim / 2, box_dim / num_bins):
            for y in np.arange(-box_dim / 2, box_dim / 2, box_dim / num_bins):
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
