import re


PASSWORD = re.compile(r'(\d{1,2})-(\d{1,2}) (.): (.*)')


def generate_file_data(file_name: str) -> str:
    with open(file_name, 'r') as file:
        for line in file:
            yield line


def is_valid_password(letter: str, value: tuple, password: str) -> bool:
    if f"{password[value[0] - 1]}{password[value[1] - 1]}".count(letter) == 1:
        return True

    return False


def main() -> int:
    count = 0
    for data in generate_file_data('../data.csv'):
        low, high, letter, password = PASSWORD.findall(data)[0]
        if is_valid_password(letter, (int(low), int(high)), password):
            count += 1

    print(f"Total valid passwords: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
    # Total valid passwords: 413
