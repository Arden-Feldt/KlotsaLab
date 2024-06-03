

class HouseHold:

    def __init__(self, tolerance, is_majority, for_sale, empty_lot):
        self.is_majority = is_majority
        self.for_sale = for_sale
        self.empty_lot = empty_lot

        if is_majority:
            self.tolerance = tolerance
        else:
            self.tolerance = 8  # or 0, unsure rn



    def show_type(self):
        if self.empty_lot:
            return " "
        elif self.is_majority:
            return "\U000025FB"
        else:
            return "\U000025FC"


