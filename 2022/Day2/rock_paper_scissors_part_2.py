from enum import Enum


class RockPaperScissors(Enum):
    A = 1
    B = 2
    C = 3


class WinLoseDraw(Enum):
    X = 0
    Y = 3
    Z = 6


class Round:
    def __init__(self, opponent: RockPaperScissors, result: WinLoseDraw):
        self.opponent = opponent
        self.result = result

    @property
    def player(self):
        if self.result == WinLoseDraw.Y:
            return self.opponent

        if self.result == WinLoseDraw.X:
            return {
                RockPaperScissors.A: RockPaperScissors.C,
                RockPaperScissors.B: RockPaperScissors.A,
                RockPaperScissors.C: RockPaperScissors.B
            }[self.opponent]

        if self.result == WinLoseDraw.Z:
            return {
                RockPaperScissors.A: RockPaperScissors.B,
                RockPaperScissors.B: RockPaperScissors.C,
                RockPaperScissors.C: RockPaperScissors.A
            }[self.opponent]

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
        game = Round(RockPaperScissors[opp], WinLoseDraw[play])
        score += game.score

    print(score)


if __name__ == "__main__":
    main()
