import numpy as np


class Binner:

    def __init__(self, frame, num_bins, highlight_bin_list):
        self.frame = frame
        self.num_bins = num_bins
        self.highlight_bin_list = highlight_bin_list

    def grey_scale_bin(self, x_dim, y_dim):
        """Used to create complex images in simulation by cutting it into manageable bins - assigns names"""

        print("started binning")

        particle_names = {}

        # Pre-calculate bin boundaries
        bin_boundaries_x = np.arange(-x_dim / 2, x_dim / 2, x_dim / self.num_bins)
        bin_boundaries_y = np.arange(-y_dim / 2, y_dim / 2, y_dim / self.num_bins)

        for particle_idx in range(self.frame.particles.N):
            particle_position = self.frame.particles.position[particle_idx]

            # Calculate bin index for particle position
            bin_index_x = np.searchsorted(bin_boundaries_x, particle_position[0], side='right') - 1
            bin_index_y = np.searchsorted(bin_boundaries_y, particle_position[1], side='right') - 1
            current_bin = bin_index_x * self.num_bins + bin_index_y

            particle_names[particle_idx] = self.highlight_bin_list[current_bin]
            # print(self.highlight_bin_list[particle_idx], end=' ')

        print("finished binning")
        return particle_names

    def black_and_white_bin(self, x_dim, y_dim):
        """Used to create complex images in simulation by cutting it into manageable bins - assigns names"""

        print("started binning")

        particle_names = {}

        # Pre-calculate bin boundaries
        bin_boundaries_x = np.arange(-x_dim / 2, x_dim / 2, x_dim / self.num_bins)
        bin_boundaries_y = np.arange(-y_dim / 2, y_dim / 2, y_dim / self.num_bins)

        for particle_idx in range(self.frame.particles.N):
            particle_position = self.frame.particles.position[particle_idx]

            # Calculate bin index for particle position
            bin_index_x = np.searchsorted(bin_boundaries_x, particle_position[0], side='right') - 1
            bin_index_y = np.searchsorted(bin_boundaries_y, particle_position[1], side='right') - 1
            current_bin = bin_index_x * self.num_bins + bin_index_y

            # Name particle based on bin membership

            particle_name = 1 if current_bin in self.highlight_bin_list else 0
            particle_names[particle_idx] = particle_name

        print("finished binning")
        return particle_names



