from typing import *
from day9constants import Map


mul = lambda x, y, z: x * y * z


def main() -> int:
    risk_level: List = []
    m = Map()
    for y, level in enumerate(m.map):
        for x in range(len(level)):
            if m.is_low_point(x, y):
                risk_level.append(m.find_basin_size(x, y, m.map[y][x]))

    risk_level.sort()
    print(mul(*risk_level[-3:]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
