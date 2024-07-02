from Graveyard.NeighborhoodSimulation import Cycle, Neighborhood


class FlightSimulator:

    def __init__(self):
        print("innited")

    def run_x_simulations(self):
        print("Start SIm")
        # impl for loop

    def run_one_simulation(self):
        # Make neighborhood of size 10
        neighborhood = Neighborhood.Neighborhood(10, .8, .05)
        cycle = Cycle.Cycle(neighborhood)

        # populate it
        neighborhood.populate_neighborhood()

        i = 0
        maxcycles = 10000
        percent_majority_over_time = [None] * maxcycles

        while neighborhood.get_percent_majority() > 50 and i < maxcycles:
            percent_majority_over_time[i] = neighborhood.get_percent_majority()
            cycle.run_cycle()
            i += 1

        print(percent_majority_over_time)


if __name__ == "__main__":
    flight_simulator = FlightSimulator()

    flight_simulator.run_one_simulation()
