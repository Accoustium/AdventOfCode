from typing import *


class POINT:
    def __init__(self, position: int, depth: int):
        self.position = position
        self.depth = depth
        self.aim = 0

    def __repr__(self):
        return f"Sub(pos={self.position}, depth={self.depth})"

    def forward(self, amount: int):
        self.position += amount
        self.depth += (self.aim * amount)

    def backward(self, amount: int):
        self.position -= amount
        self.depth -= (self.aim * amount)

    def down(self, amount: int):
        self.aim += amount

    def up(self, amount: int):
        self.aim -= amount

    def move(self, movement: AnyStr):
        direction, amount = movement.split(" ")
        amount = int(amount)

        eval(f"self.{direction}({amount})")


def read_data() -> Generator:
    with open('day2part2.txt', 'r') as file:
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
