from typing import *


OPEN = "[{(<"
CLOSE = "]})>"
MATCH = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
CORRUPT_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
INCOMPLETE_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def generate_chunk():
    with open("day10data.txt", "r") as file:
        for line in file:
            yield line.strip()


class Chunk:
    def __init__(self, line: AnyStr):
        self.syntax = list()
        self.points = 0
        self.incomplete = False

        for char in line:
            if char in OPEN:
                self.syntax.append(char)
            elif char == MATCH[self.syntax[-1]]:
                self.syntax.pop(-1)
            else:
                self.points = CORRUPT_POINTS[char]
                break

        if self.points == 0 and len(self.syntax) > 0:
            self.incomplete = True
            self.close_chunk()

    def __repr__(self):
        return f"Chunk({self.points})"

    def close_chunk(self):
        for char in self.syntax[-1::-1]:
            self.points *= 5
            self.points += INCOMPLETE_POINTS[MATCH[char]]
