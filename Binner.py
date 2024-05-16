import numpy as np

from Testing import box_dim


class Binner:

    def __init__(self, frame, num_bins, highlight_bin_list):
        self.frame = frame
        self.num_bins = num_bins
        self.highlight_bin_list = highlight_bin_list

    def binning_method(self):
        particle_names = {}

        """Used to create comple images in simulation by cutting it into managable bins - assigns names"""
        for particle_idx in range(self.frame.particles.N):
            particle_position = self.frame.particles.position[particle_idx]

            current_bin = 0

            for x in np.arange(-box_dim / 2, box_dim / 2, box_dim / self.num_bins):
                for y in np.arange(-box_dim / 2, box_dim / 2, box_dim / self.num_bins):
                    # check to see if particle is in current bin
                    if x <= particle_position[0] < x + box_dim / self.num_bins and y <= \
                            particle_position[1] < y + box_dim / self.num_bins:
                        # name particle given on if bin is in binlist
                        particle_name = 1 if current_bin in self.highlight_bin_list else 0
                        # Store the particle name in the dictionary
                        particle_names[particle_idx] = particle_name
                    current_bin += 1
                    y += box_dim / self.num_bins
                x += box_dim / self.num_bins
        return particle_names
