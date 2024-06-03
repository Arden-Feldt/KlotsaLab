import random

from WhiteFlight import HouseHold


class Neighborhood:
    def __init__(self, size):
        self.neighborhood = [[None for _ in range(size)] for _ in range(size)]

    def populate_neighborhood(self, majority_percent, for_sale_per, empty_lot_per):
        for i, row in enumerate(self.neighborhood):
            for j in range(len(row)):
                self.neighborhood[i][j] = (
                    HouseHold.HouseHold(
                        8,
                        self.biased_random_boolean(majority_percent),
                        False,
                        False))

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



    def biased_random_boolean(self, bias=0.5):
        """
        Returns a boolean value with a given bias towards True.

        :param bias: A float between 0 and 1 representing the probability of True.
                     For example, bias=0.7 means a 70% chance of returning True.
        :return: A boolean value, True or False, with the specified bias.
        """
        return random.choices([True, False], weights=[bias, 1 - bias], k=1)[0]


