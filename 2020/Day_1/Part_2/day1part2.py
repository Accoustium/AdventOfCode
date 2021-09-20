def read_data(file_name: str) -> list:
    f = open(file_name, 'r')
    return f.read().split('\n')


def check_2020(first: int, second: int, third: int) -> bool:
    if first + second + third == 2020:
        return True

    return False


def main() -> int:
    data = read_data('../data.csv')
    data_copy = data.copy()
    data_double_copy = data.copy()

    for idx, first_int in enumerate(data):
        for idx2, second_int in enumerate(data_copy[idx + 1:]):
            for third_int in data_double_copy[idx2 + 1:]:
                if check_2020(int(first_int), int(second_int), int(third_int)):
                    print(f"{first_int} * {second_int} * {third_int} = {int(first_int) * int(second_int) * int(third_int)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
    # 395 * 198 * 1427 = 111605670
