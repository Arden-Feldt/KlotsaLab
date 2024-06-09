import gsd

from GSDModification import GSDCopier, CameraSetter, RWgsdChecker
from GSDModification.ColumnChecker import ColumnChecker


def copy_gsd(input_gsd, output_gsd):
    gsd_copier = GSDCopier.GSDCopier(input_gsd, output_gsd)
    gsd_copier.copy()


def set_camera(input_gsd, output_gsd, right_shift, up_shift):
    camset = CameraSetter.CameraSetter(input_gsd, output_gsd)
    camset.set_cam(get_x_box_dim(input_gsd), get_y_box_dim(input_gsd), right_shift, up_shift)


def check_write(gsd):
    checker = RWgsdChecker.RWgsdChecker(gsd)
    checker.check()


def get_x_box_dim(input_gsd):
    with gsd.hoomd.open(name=input_gsd, mode="r") as file:
        for frame_index, frame in enumerate(file):
            box = frame.configuration.box
            return box[0]  # x value


def get_y_box_dim(input_gsd):
    with gsd.hoomd.open(name=input_gsd, mode="r") as file:
        for frame_index, frame in enumerate(file):
            box = frame.configuration.box
            return box[1]  # y value


def get_final_frame(gsd_file):
    with gsd.hoomd.open(name=gsd_file, mode='r') as file:
        # Get the number of frames
        return len(file)


def print_columns(gsd_path):
    printer = ColumnChecker(gsd_path)
    printer.print_columns()


class ModifierManager:
    def __init__(self):
        """inits the modifier manager"""
        # this shit doth nothing rn, but the static funtions^ are helpful
