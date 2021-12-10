from typing import *
import statistics


def get_crab_data() -> List[int]:
    with open("day7data.txt", "r") as file:
        return list(map(int, file.read().split(",")))


class Crab:
    def __init__(self):
        self.crab_list = get_crab_data()
        self.mean = round(statistics.mean(self.crab_list))

    def __repr__(self):
        return f"Crab({self.mean})"

    def find_diff(self, difference: int=None) -> int:
        diff = 0
        if difference is None:
            difference = self.mean

        for crab in self.crab_list:
            n = abs(difference - crab)
            diff += (n * (n + 1)) / 2

        return diff
