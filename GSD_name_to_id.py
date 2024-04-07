import gsd.hoomd
import final_frame_id_lock
import typeID_changer
from ImageReader import ImageReader


def gsd_render(input_gsd, output_gsd, num_bins, image_path):
    print("started")

    # Array for particle names
    particle_names = {}
    box_dim = 361.8006286621094

    # Read in the file with the intent to name
    with gsd.hoomd.open(name=input_gsd, mode="r") as file:

        # Give Each Particle a Name
        for frame_index, frame in enumerate(file):
            if frame_index == 349:
                # Locks colors in accordance to image
                colorlist = ImageReader.image_reader(image_path, num_bins)
                bin_list = ImageReader.color_to_binlist(colorlist)
                particle_names = final_frame_id_lock.binning_method(frame, num_bins, box_dim, bin_list)
                print(particle_names)

        # Create a new GSD file for writing and set typeid given name
        with gsd.hoomd.open(name=output_gsd, mode="w") as modified_file:

            # Looping through and update typeID to reflect name
            for frame_index, frame in enumerate(file):
                # Write the modified frame to the new GSD file
                modified_file.append(typeID_changer.id_update(frame, particle_names))

    print("finished")
