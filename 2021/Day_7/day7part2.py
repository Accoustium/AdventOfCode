from day7constants import Crab


class NewCrab(Crab):
    def __init__(self):
        super(NewCrab, self).__init__()

    def find_diff(self, difference: int = None) -> int:
        diff = 0
        if difference is None:
            difference = self.mean

        for crab in self.crab_list:
            n = abs(difference - crab)
            diff += (n * (n + 1)) / 2

        return diff


def main() -> int:
    c = NewCrab()
    print(
        min(
            [
                (c.find_diff(test), test) for test in range(1, len(c.crab_list))
            ]
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
