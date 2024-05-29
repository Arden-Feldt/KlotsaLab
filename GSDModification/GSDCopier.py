import gsd.hoomd


class GSDCopier:
    def __init__(self, input_gsd, output_gsd):
        self.read_in_gsd = input_gsd
        self.output_gsd = output_gsd

    def copy(self):
        """copies one gsd to another, bar for bar, frame by frame"""

        print("started copy")

        with gsd.hoomd.open(name=self.read_in_gsd, mode="r") as file:
            with gsd.hoomd.open(name=self.output_gsd, mode="w") as modified_file:
                # Looping through and update typeID to reflect name
                for frame in file:
                    # Write the modified frame to the new GSD file
                    modified_file.append(frame)

        print("finished copy")
