import gsd.hoomd

import camera_set
import final_frame_id_lock
import typeID_changer

if __name__ == '__main__':
    print("started")

    # Array for particle names
    particle_names = {}
    box_dim = 361.8006286621094

    # Read in the file with the intent to name
    with gsd.hoomd.open(name="modifiable_UNC_gsd.gsd", mode="r") as file:

        # Give Each Particle a Name
        for frame_index, frame in enumerate(file):
            if frame_index == 349:
                particle_names = final_frame_id_lock.particle_namer(frame)

        # Create a new GSD file for writing and set typeid given name
        with gsd.hoomd.open(name="clone_of_modifile.gsd", mode="w") as modified_file:

            # Looping through and update typeID to reflect name
            for frame_index, frame in enumerate(file):
                # Write the modified frame to the new GSD file
                modified_file.append(typeID_changer.id_update(frame, particle_names))

    print(particle_names)
    print("finished")