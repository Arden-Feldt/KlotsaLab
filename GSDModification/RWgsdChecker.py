import gsd.hoomd


class RWgsdChecker:
    def __init__(self, gsd):
        self.gsd = gsd

    def check(self):
        try:
            # Try to open the file in read-write mode
            with gsd.hoomd.open(name=self.gsd, mode="r+") as file:
                for frame_index, frame in enumerate(file):
                    # Perform a write operation to check if the file is read-only
                    file.append(frame)
                    # TODO: make this not double the size permenantly

            print(f"The file '{self.gsd}' is read-write.")

        except PermissionError:
            print(f"The file '{self.gsd}' is read-only.")
