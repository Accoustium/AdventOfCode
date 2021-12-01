from typing import Generator, List, AnyStr


def generate_measure() -> Generator:
    data: List[AnyStr] = open('day1part2.txt', 'r').read().split("\n")
    previous_measure = None
    length = len(data)
    for idx in range(length):
        if length - idx >= 3:
            yield previous_measure, sum(list(map(int, data[idx: idx+3])))
            previous_measure = sum(list(map(int, data[idx: idx+3])))


def main() -> int:
    increased = 0
    for old, new in generate_measure():
        if old is None:
            continue

        if new > old:
            increased += 1

    print(increased)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
