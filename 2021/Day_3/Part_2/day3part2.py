from typing import *


class ErrorCode:
    def __init__(self):
        self.oxygen: List[AnyStr] = list()
        self.co2scrubber: List[AnyStr] = list()

    def process_oxygen(self, input_code: AnyStr, code: AnyStr):
        if input_code[0] == code:
            self.oxygen.append(input_code)

    def process_co2(self, input_code: AnyStr, code: AnyStr):
        if input_code[0] == code:
            self.co2scrubber.append(input_code)

    def finish_oxygen(self):
        idx = 1
        while len(self.oxygen) > 1:
            position = ""
            leading = "1"
            for code in self.oxygen:
                position += code[idx]

            if position.count("0") > position.count("1"):
                leading = "0"

            self.oxygen = list(filter(lambda x: x[idx] == leading, self.oxygen))
            idx += 1

    def finish_co2(self):
        while len(self.co2scrubber) > 1:
            idx = 1
            while len(self.co2scrubber) > 1:
                position = ""
                leading = "0"
                for code in self.co2scrubber:
                    position += code[idx]

                if position.count("1") < position.count("0"):
                    leading = "1"

                self.co2scrubber = list(filter(lambda x: x[idx] == leading, self.co2scrubber))
                idx += 1

    def life_support(self):
        return int(self.oxygen[0], 2) * int(self.co2scrubber[0], 2)


def read_error_data() -> Tuple:
    with open('day3part2.txt', 'r') as file:
        data = file.read().split('\n')

    processed_data: List[AnyStr] = []
    for idx in range(len(data[0])):
        inpt = ""
        for new_idx in range(len(data)):
            inpt += data[new_idx][idx]
        processed_data.append(inpt)

    return processed_data[0], data


def main() -> int:
    life = ErrorCode()
    first_line, whole_data = read_error_data()
    for code in whole_data:
        if first_line.count("1") > first_line.count("0"):
            life.process_oxygen(code, "1")
            life.process_co2(code, "0")
        else:
            life.process_oxygen(code, "0")
            life.process_co2(code, "1")

    life.finish_oxygen()
    life.finish_co2()

    print(life.life_support())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
