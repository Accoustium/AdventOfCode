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
        print(d.output, output, int("".join(list(map(lambda x: str(x.number), d.output)))))
        output += int("".join(list(map(lambda x: str(x.number), d.output))))

    print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
