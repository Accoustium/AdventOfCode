from copy import copy
from typing import *
from day6constants import LanturnFish


def read_data() -> Generator:
    data = open("day6data.txt", "r").read()
    for new in data.split(","):
        yield new


def main() -> int:
    fish_array = list()
    for fish in read_data():
        fish_array.append(LanturnFish(int(fish)))

    length, old_gen = len(fish_array), []
    new_gen = copy(old_gen)
    for _ in range(256):
        new_fish = list()
        if _ < 10:
            for fish in fish_array:
                if fish.next_day():
                    new_fish.append(LanturnFish())

        fish_array.extend(new_fish)
        if _ < 7:
            old_gen.append(len(new_fish))
            length += old_gen[_ % 7]
        elif _ <= 9:
            new_gen = copy(old_gen)
            length += old_gen[_ % 7]
        else:
            new_gen[_ % 7] += old_gen[(_ % 7) - 2]
            old_gen[(_ % 7) - 2] = new_gen[(_ % 7) - 2]
            length += new_gen[_ % 7]

    print(length)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
