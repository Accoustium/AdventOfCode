from typing import Generator
from string import ascii_letters

def read_rucksack() -> Generator:
    with open("data.txt", "r") as f:
        for new_pack in f:
            yield new_pack


def find_value(value: str) -> int:
    return ascii_letters.index(value) + 1


def main():
    total = 0

    for ruck in read_rucksack():
        middle = len(ruck) // 2

        first = ruck[:middle]
        second = ruck[middle:]

        matching = set(first).intersection(set(second))
        for item in matching:
            total += find_value(item)

    print(total)

if __name__ == "__main__":
    main()
