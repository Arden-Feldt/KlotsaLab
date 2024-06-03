
class Cycle:

    def __init__(self):
        self.cycle_num = 0

    def run_cycle(self, neighborhood):
        print("Starting Cycle: ", self.cycle_num)
        self.cycle_num += 1
        print("The Neighborhood is ", neighborhood.get_percent_majority(), "% the majority group.")

        neighborhood.print_neighborhood()

        neighborhood.move_out()

        neighborhood.generate_fill()

        neighborhood.repopulate_sold()

