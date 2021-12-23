from typing import *


def read_map_data() -> Generator:
    with open("day9data.txt", "r") as file:
        for line in file:
            yield line


class Map:
    def __init__(self):
        self.map: List[List[int]] = []
        for line in read_map_data():
            self.map.append(list(map(int, line.strip())))

    def is_low_point(self, x, y) -> bool:
        for _x, _y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            try:
                if all([y + _y > -1, x + _x > -1]):
                    if self.map[y + _y][x + _x] <= self.map[y][x]:
                        return False
            except IndexError:
                continue

        return True

    def find_basin_size(self, x, y, original) -> int:
        if x < 0 or y < 0:
            return 0

        if original == 9:
            return 0

        self.map[y][x] = 9
        basin = 0
        if x - 1 > -1:
            basin = self.find_basin_size(x - 1, y, self.map[y][x - 1])
        if y -1 > -1:
            basin += self.find_basin_size(x, y - 1, self.map[y - 1][x])
        if x + 1 < len(self.map[y]):
            basin += self.find_basin_size(x + 1, y, self.map[y][x + 1])
        if y + 1 < len(self.map):
            basin += self.find_basin_size(x, y + 1, self.map[y + 1][x])

        # self.map[y][x] = original
        return basin + 1
