from typing import *
import re


FIND_BOARD = re.compile(r'(\d{1,2})\s{0,2}')


class Bingo:
    def __init__(self, board: AnyStr):
        self.board: List = list(map(int, FIND_BOARD.findall(board)))
        self.marked_numbers: Set = set()
        self.vertical_wins: List[Set] = [
            set(self.board[x::5]) for x in range(5)
        ]
        self.horizontal_wins: List[Set] = [
            set(self.board[x:x + 5]) for x in range(0, len(self.board), 5)
        ]
        self.diagonal_wins: List[Set] = [
            set(self.board[::6]), set(self.board[4:-2:4])
        ]

    def __repr__(self):
        return f"Board()"

    def new_number(self, number: int):
        if number in self.board:
            self.marked_numbers.add(number)

        if self._check_for_win():
            print(self._calculate_win(number))
            raise SystemExit(0)

    def _check_for_win(self):
        for check in self.vertical_wins:
            if self._check_sets(check):
                return True

        for check in self.horizontal_wins:
            if self._check_sets(check):
                return True

        for check in self.diagonal_wins:
            if self._check_sets(check):
                return True

        return False

    def _check_sets(self, set_1: set):
        return set_1.difference(self.marked_numbers) == set()

    def _calculate_win(self, multiply_number: int):
        return sum(
            set(self.board).difference(self.marked_numbers)
        ) * multiply_number


def read_data() -> List[AnyStr]:
    with open('day4part1.txt', 'r') as file:
        data = file.read().split("\n\n")

    return data


def main() -> int:
    numbers = None
    boards = list()
    for line in read_data():
        if numbers is None:
            numbers = list(map(int, line.split(",")))
        else:
            boards.append(Bingo(line))

    for num in numbers:
        for board in boards:
            board.new_number(num)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
