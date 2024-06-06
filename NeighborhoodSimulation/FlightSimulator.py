from NeighborhoodSimulation import Neighborhood, Cycle


def main():
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
    main()
