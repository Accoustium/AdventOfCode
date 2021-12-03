from typing import *


class ErrorCode:
    def __init__(self):
        self.gamma = ""
        self.epsilon = ""

    def process_code(self, error_code: AnyStr):
        if error_code.count("1") > error_code.count("0"):
            self.gamma += "1"
            self.epsilon += "0"
        else:
            self.gamma += "0"
            self.epsilon += "1"

    def power_consumption(self):
        return int(self.gamma, 2) * int(self.epsilon, 2)


def read_error_data() -> List[AnyStr]:
    with open('day3part1.txt', 'r') as file:
        data = file.read().split('\n')

    processed_data: List[AnyStr] = []
    for idx in range(len(data[0])):
        inpt = ""
        for new_idx in range(len(data)):
            inpt += data[new_idx][idx]
        processed_data.append(inpt)

    return processed_data


def main() -> int:
    power = ErrorCode()
    for code in read_error_data():
        power.process_code(code)

    print(power.power_consumption())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
