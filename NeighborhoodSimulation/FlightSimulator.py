from NeighborhoodSimulation import Neighborhood, Cycle


def main():
    # Make neighborhood of size 10
    neighborhood = Neighborhood.Neighborhood(30, .8, .05)
    cycle = Cycle.Cycle()

    # populate it
    neighborhood.populate_neighborhood()

    while neighborhood.get_percent_majority() > 50:
        cycle.run_cycle(neighborhood)


if __name__ == "__main__":
    main()
