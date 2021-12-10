from day7constants import Crab


def main() -> int:
    c = Crab()
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
