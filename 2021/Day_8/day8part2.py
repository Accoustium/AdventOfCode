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
        for out in d.signal:
            print(out, out.display_string)
            if out.number is None:
                out.hard_number()
        # output += int("".join(map(lambda x: str(x.number), d.output)))
        print()

    print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
