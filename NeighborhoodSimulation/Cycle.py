
class Cycle:

    def __init__(self, neighborhood):
        self.cycle_num = 0
        self.neighborhood = neighborhood

    def run_cycle(self):
        print("Starting Cycle: ", self.cycle_num)
        self.cycle_num += 1
        print("The Neighborhood is ", self.neighborhood.get_percent_majority(), "% the majority group.")

        self.neighborhood.print_neighborhood()

        self.neighborhood.move_out()

        # neighborhood.generate_fill()

        self.neighborhood.repopulate_sold()

    def cycle_still_going(self, neighborhood, old_neighborhood):
        if neighborhood == old_neighborhood:
            return False
        return True

    def get_cycle_num(self):
        return self.cycle_num



