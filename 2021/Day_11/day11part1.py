from typing import *

from day11constants import read_initial_map, Octopus, Map, FLASH_QUEUE


def flash(map_data: Map, obj: Octopus):
    point = obj.loca
    for y_ in [-1, 0, 1]:
        for x_ in [-1, 0, 1]:
            if (
                0 <= point.y + y_ < map_data.height and
                0 <= point.x + x_ < map_data.width
            ):
                try:
                    map_data.data[point.y + y_][point.x + x_] += 1
                except IndexError:
                    continue


def main() -> int:
    base_map = read_initial_map()

    steps = list()
    while len(steps) < 100:
        flash_ = 0
        for y_ in range(base_map.height):
            for x_ in range(base_map.width):
                base_map.data[y_][x_] += 1

        while not FLASH_QUEUE.empty():
            octopus_obj = FLASH_QUEUE.get()
            flash(base_map, octopus_obj)

        for y_ in range(len(base_map.data)):
            for x_ in range(len(base_map.data[y_])):
                if base_map.data[y_][x_].flash:
                    flash_ += 1
                    base_map.data[y_][x_].reset()

        steps.append(flash_)

    print(sum(steps))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
