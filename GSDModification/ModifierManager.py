from GSDModification import GSDCopier, CameraSetter, RWgsdChecker


def copy(input_gsd, output_gsd):
    gsd_copier = GSDCopier.GSDCopier(input_gsd, output_gsd)
    gsd_copier.copy()


def set_camera(input_gsd, output_gsd):
    camset = CameraSetter.CameraSetter(input_gsd, output_gsd)
    camset.set_cam()


def check_write(gsd):
    checker = RWgsdChecker.RWgsdChecker(gsd)
    checker.check()


class ModifierManager:
    def __init__(self):
        """inits the modifier manager"""
        # this shit doth nothing rn, but the static funtions^ are helpful
