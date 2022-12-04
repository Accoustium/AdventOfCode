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
    ruck = read_rucksack()

    try:
        while True:
            ruck_one = next(ruck)
            ruck_two = next(ruck)
            ruck_three = next(ruck)

            ruck_union = set(ruck_one.strip()).intersection(set(ruck_two.strip())).intersection(
                set(ruck_two.strip()).intersection(set(ruck_three.strip()))).intersection(
                set(ruck_three.strip()).intersection(set(ruck_one.strip())))

            for item in ruck_union:
                total += find_value(item)

    except StopIteration:
        print(total)

if __name__ == "__main__":
    main()
