from typing import Generator


def generate_data() -> Generator:
    previous = None
    with open('day1part1.txt', 'r') as file:
        for line in file:
            yield previous, int(line)
            previous = int(line)


def main() -> int:
    increased = 0
    for old, new in generate_data():
        if old is None:
            continue

        if new > old:
            increased += 1

    print(increased)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
