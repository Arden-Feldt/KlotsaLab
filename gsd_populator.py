import gsd.hoomd
import final_frame_id_lock
import typeID_changer

read_in_gsd = "centered_GSD.gsd"
output_gsd = "output.gsd"

if __name__ == '__main__':
    print("started")

    with gsd.hoomd.open(name=read_in_gsd, mode="r") as file:
        with gsd.hoomd.open(name=output_gsd, mode="w") as modified_file:
            # Looping through and update typeID to reflect name
            for frame in file:
                # Write the modified frame to the new GSD file
                modified_file.append(frame)

    print("finished")
