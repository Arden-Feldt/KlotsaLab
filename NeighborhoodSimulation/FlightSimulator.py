from NeighborhoodSimulation import Neighborhood, Cycle


def main():
    # Make neighborhood of size 10
    neighborhood = Neighborhood.Neighborhood(10, .8, .05)
    cycle = Cycle.Cycle()

    # populate it
    neighborhood.populate_neighborhood()

    i = 0
    while neighborhood.get_percent_majority() > 50 and i < 10000:
        cycle.run_cycle(neighborhood)
        i += 1

    cycle.run_cycle(neighborhood)


if __name__ == "__main__":
    main()
