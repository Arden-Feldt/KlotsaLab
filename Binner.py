import numpy as np

from Testing import box_dim


class Binner:

    def __init__(self, frame, num_bins, highlight_bin_list):
        self.frame = frame
        self.num_bins = num_bins
        self.highlight_bin_list = highlight_bin_list

    def optimize_binning(self):
        """Used to create complex images in simulation by cutting it into manageable bins - assigns names"""

        print("started opt-binning")

        particle_names = {}

        # Pre-calculate bin boundaries
        bin_boundaries_x = np.arange(-box_dim / 2, box_dim / 2, box_dim / self.num_bins)
        bin_boundaries_y = np.arange(-box_dim / 2, box_dim / 2, box_dim / self.num_bins)

        for particle_idx in range(self.frame.particles.N):
            particle_position = self.frame.particles.position[particle_idx]

            # Calculate bin index for particle position
            bin_index_x = np.searchsorted(bin_boundaries_x, particle_position[0], side='right') - 1
            bin_index_y = np.searchsorted(bin_boundaries_y, particle_position[1], side='right') - 1
            current_bin = bin_index_x * self.num_bins + bin_index_y

            # Name particle based on bin membership
            particle_name = 1 if current_bin in self.highlight_bin_list else 0
            particle_names[particle_idx] = particle_name

        print("finished opt-binning")
        return particle_names

    '''
    def particle_namer(self, frame):
        """Splits the simulation down the middle - used for testing"""
        # Splits the simulation down the middle by the last frame
        for particle_idx in range(frame.particles.N):
            particle_position = frame.particles.position[particle_idx]
            # Generate particle name based on the condition
            particle_name = 1 if particle_position[0] >= 0 else 0
            # Store the particle name in the dictionary
            particle_names[particle_idx] = particle_name
        return particle_names
    '''