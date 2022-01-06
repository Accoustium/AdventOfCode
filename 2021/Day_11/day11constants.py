from typing import *
from collections import namedtuple
from queue import Queue


POINT = namedtuple("POINT", "x y")
FLASH_QUEUE = Queue()


class Octopus:
    def __init__(self, init_level: str, point: POINT, queue: Queue):
        self.light_level = int(init_level)
        self.loca: POINT = point
        self.queue: Queue = queue
        self.flash = False

    def __repr__(self):
        return f"Octopus({self.light_level})"

    def __str__(self):
        return f"{self.light_level}"

    def __add__(self, other):
        self.light_level = self.light_level + 1
        if self.light_level > 9 and not self.flash:
            self.flash = True
            self.queue.put(self)

        return self

    def reset(self):
        self.light_level = 0
        self.flash = False


class Map:
    def __init__(self, map_data: List[AnyStr], queue: Queue):
        self.data: List[List[Octopus]] = list()
        self.queue: Queue = queue

        self._load_map(map_data)
        self.height = len(self.data)
        self.width = len(self.data[0])

    def __repr__(self):
        return "\n".join(map(lambda x: "".join(map(str, x)), self.data))

    def _load_map(self, map_info: List[AnyStr]):
        for y_, line in enumerate(map_info):
            self.data.append(list())
            for x_, value in enumerate(line):
                self.data[y_].append(Octopus(value, POINT(x_, y_), self.queue))


def read_initial_map() -> Map:
    with open("day11data.txt", "r") as file:
        data = file.read().split("\n")

    map_ = Map(data, FLASH_QUEUE)

    return map_
