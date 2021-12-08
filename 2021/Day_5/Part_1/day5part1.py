import re
import math
from collections import namedtuple
from typing import *


VENT_LOCATION = re.compile(r'(\d{1,3}),(\d{1,3}) -> (\d{1,3}),(\d{1,3})')


class VENTLINE(namedtuple("VENTLINE", "x1 y1 x2 y2")):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()

    @property
    def change_in_x(self) -> Union[bool, int]:
        try:
            return (self.x2 - self.x1) / (self.y2 - self.y1)
        except ZeroDivisionError:
            return 1 if self.x1 < self.x2 else -1

    @property
    def change_in_y(self) -> Union[bool, int]:
        try:
            return (self.y2 - self.y1) / (self.x2 - self.x1)
        except ZeroDivisionError:
            return 1 if self.y1 < self.y2 else -1

    @property
    def length(self) -> float:
        return math.sqrt(
            (self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2
        )


class HydrothermalVents:
    def __init__(self, x1: int, y1: int):
        self.x = x1
        self.y = y1
        self.map: List[List[int]] = []
        for y in range(y1):
            self.map.append([0] * x1)

    def __repr__(self):
        return f"HydrothermalVents(x={self.x}, y={self.y})"

    def update_vent(self, vent: VENTLINE):
        start = (vent.x1 - 1, vent.y1 - 1)
        self.map[int(start[1])][int(start[0])] += 1
        for _ in range(int(vent.length)):
            start = (start[0] + vent.change_in_x, start[1] + vent.change_in_y)
            self.map[int(start[1])][int(start[0])] += 1

    @property
    def danger_zone(self):
        total = 0
        for y_idx in range(self.y):
            for x_idx in range(self.x):
                if self.map[y_idx][x_idx] >= 2:
                    total += 1

        return total


def read_data() -> List[VENTLINE]:
    data = []
    with open("day5part1.txt", 'r') as file:
        for line in file:
            data.append(
                VENTLINE(
                    *list(map(int, VENT_LOCATION.findall(line)[0]))
                )
            )

    return data


def find_map_coords(map_data: List[VENTLINE]) -> Tuple:
    x_max, y_max = 0, 0
    for coord in map_data:
        x_max = max(x_max, coord.x1, coord.x2)
        y_max = max(y_max, coord.y1, coord.y2)

    return x_max, y_max


def main() -> int:
    map_data = read_data()
    x_max, y_max = find_map_coords(map_data)

    map = HydrothermalVents(x_max, y_max)

    for vent in map_data:
        if vent.change_in_y == 0 or vent.change_in_x == 0:
            map.update_vent(vent)

    print(map.danger_zone)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
