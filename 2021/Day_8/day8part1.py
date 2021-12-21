from typing import *
from day8constants import Display


def generate_display() -> Generator:
    with open("day8data.txt", "r") as file:
        for display in file:
            yield display


def main() -> int:
    output = 0
    for disp in generate_display():
        d = Display(disp)
        for out in d.output:
            if out.number is not None:
                output += 1

    print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
