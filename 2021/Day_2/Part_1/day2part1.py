from typing import *


class POINT:
    def __init__(self, position: int, depth: int):
        self.position = position
        self.depth = depth

    def __repr__(self):
        return f"Sub(pos={self.position}, depth={self.depth})"

    def forward(self, amount: int):
        self.position += amount

    def backward(self, amount: int):
        self.position -= amount

    def down(self, amount: int):
        self.depth += amount

    def up(self, amount: int):
        self.depth -= amount

    def move(self, movement: AnyStr):
        direction, amount = movement.split(" ")
        amount = int(amount)

        eval(f"self.{direction}({amount})")


def read_data() -> Generator:
    with open('day2part1.txt', 'r') as file:
        for line in file:
            yield line


def main() -> int:
    sub = POINT(0, 0)
    for line in read_data():
        print(sub, line)
        sub.move(line)

    print(sub.position * sub.depth)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
