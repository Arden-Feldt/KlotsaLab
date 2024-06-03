from WhiteFlight import Neighborhood


def main():
    # Make neighborhood of size 10
    neighborhood = Neighborhood.Neighborhood(30)

    # populate it
    neighborhood.populate_neighborhood(.8, .9, .9)
    # Percent white ^ https://www.brookings.edu/articles/even-as-metropolitan-areas-diversify-white-americans-
    #                 still-live-in-mostly-white-neighborhoods/

    # print the population
    neighborhood.print_neighborhood()

    print(neighborhood.get_percent_majority())


if __name__ == "__main__":
    main()
