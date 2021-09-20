def read_data(file_name: str) -> list:
    f = open(file_name, 'r')
    return f.read().split('\n')


def check_2020(first: int, second: int) -> bool:
    if first + second == 2020:
        return True

    return False


def main() -> int:
    data = read_data('../data.csv')
    data_copy = data.copy()

    for idx, first_int in enumerate(data):
        for second_int in data_copy[idx + 1:]:
            if check_2020(int(first_int), int(second_int)):
                print(f"{first_int} * {second_int} = {int(first_int) * int(second_int)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
    # 211 * 1809 = 381699
