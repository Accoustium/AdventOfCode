from enum import Enum


class RockPaperScissors(Enum):
    A = 1
    B = 2
    C = 3
    X = 1
    Y = 2
    Z = 3


class WinLoseDraw(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3


class Round:
    def __init__(self, opponent: RockPaperScissors, player: RockPaperScissors):
        self.opponent = opponent
        self.player = player

    @property
    def result(self) -> WinLoseDraw:
        if self.opponent.value == self.player.value:
            return WinLoseDraw.DRAW

        if (
                (self.opponent == RockPaperScissors.A and self.player == RockPaperScissors.Y) or
                (self.opponent == RockPaperScissors.B and self.player == RockPaperScissors.Z) or
                (self.opponent == RockPaperScissors.C and self.player == RockPaperScissors.X)
        ):
            return WinLoseDraw.WIN

        return WinLoseDraw.LOSE

    @property
    def score(self) -> int:
        return self.player.value + self.result.value


def read_data():
    with open("data.txt", "r") as f:
        for new_line in f:
            yield new_line


def main():
    score = 0
    for round in read_data():
        opp, play = round.strip().split(" ")
        game = Round(RockPaperScissors[opp], RockPaperScissors[play])
        score += game.score

    print(score)


if __name__ == "__main__":
    main()
