import random

from NeighborhoodSimulation import HouseHold


class Neighborhood:
    def __init__(self, size, majority_percent, empty_lot_per):
        self.neighborhood = [[None for _ in range(size)] for _ in range(size)]
        self.majority_percent = majority_percent
        self.empty_lot_per = empty_lot_per

    def populate_neighborhood(self):
        for i, row in enumerate(self.neighborhood):
            for j in range(len(row)):
                self.neighborhood[i][j] = (
                    HouseHold.HouseHold(
                        1,
                        self.biased_random_boolean(self.majority_percent),
                        False,
                        self.biased_random_boolean(self.empty_lot_per)))

    def get_neighborhood(self):
        return self.neighborhood

    def print_neighborhood(self):
        for row in self.neighborhood:
            for house in row:
                print(house.show_type(), end=" ")
            print("")

    def get_percent_majority(self):
        result = 0
        i = 0
        for row in self.neighborhood:
            for house in row:
                i += 1
                if house.show_type() == "\U000025FB":
                    result += 1
        return round((result / i) * 100)

    def move_out(self):
        for i, row in enumerate(self.neighborhood):
            for j in range(len(row)):
                non_major_neighbor = 0

                # List of relative neighbor positions
                neighbors = [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                    (1, -1), (1, 0), (1, 1)
                ]

                for dx, dy in neighbors:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(self.neighborhood) and 0 <= nj < len(row):
                        if self.neighborhood[ni][nj].check_non_major():
                            non_major_neighbor += 1

                # diff
                if self.neighborhood[i][j].get_tolerance() < non_major_neighbor: # TODO: ignore empty lots
                    self.neighborhood[i][j].set_sold(True)

    def biased_random_boolean(self, bias=0.5):
        """
        Returns a boolean value with a given bias towards True.

        :param bias: A float between 0 and 1 representing the probability of True.
                     For example, bias=0.7 means a 70% chance of returning True.
        :return: A boolean value, True or False, with the specified bias.
        """
        return random.choices([True, False], weights=[bias, 1 - bias], k=1)[0]

    # TODO: Figure out why this isn't repoping sold houses
    def repopulate_sold(self):
        for i, row in enumerate(self.neighborhood):
            for j in range(len(row)):
                if self.neighborhood[i][j].get_sold():
                    self.neighborhood[i][j] = (
                        HouseHold.HouseHold(
                            random.randint(1, 8),
                            self.biased_random_boolean(self.majority_percent),
                            False,
                            False))

    def generate_fill(self):
        for i, row in enumerate(self.neighborhood):
            for j in range(len(row)):
                self.neighborhood[i][j] = (
                    HouseHold.HouseHold(
                        random.randint(1, 8),
                        False,
                        False,
                        False))
