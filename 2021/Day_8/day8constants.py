import re
from typing import *


DISPLAY_OUTPUT = re.compile(r'([a-g]{2,7})')
DISPLAY = {
    "acedgfb": 8,
    "cdfbe": 5,
    "gcdfa": 2,
    "fbcad": 3,
    "dab": 7,
    "cefabd": 9,
    "cdfgeb": 6,
    "eafb": 4,
    "cagedb": 0,
    "ab": 1,
}


class Number(object):
    def __init__(self, display: str):
        self.display_string: str = display
        self.number: Optional[int, None] = None
        self.easy_number()

    def __repr__(self):
        return f"Number({self.number})"

    def easy_number(self):
        for display in DISPLAY:
            if len(display) != 6 and len(display) != 5:
                if len(display) == len(self.display_string):
                    self.number = DISPLAY[display]

    def hard_number(self): ...


class Display(object):
    def __init__(self, display_code: str):
        display = DISPLAY_OUTPUT.findall(display_code)
        self.signal: List[Number] = list(map(Number, display[:10]))
        self.output: List[Number] = list(map(Number, display[10:]))
        self.find_nine()
        self.find_six()
        self.find_five()
        self.find_three()
        self.find_two()
        self.find_zero()

        for num in self.output:
            if num.number is None:
                num.number = self.find_string(num.display_string)

    def __repr__(self):
        return f"""Display({''.join(
            map(lambda x: str(x.number), self.signal)
        )} | {''.join(
            map(lambda x: str(x.number), self.output)
        )})"""

    def find_number(self, number: int) -> str:
        for num in self.signal:
            if num.number == number:
                return num.display_string

    def find_string(self, display_string: str) -> int:
        for num in self.signal:
            if num.number not in [1, 8, 7, 4]:
                if len(display_string) == len(num.display_string):
                    if set(display_string).difference(set(num.display_string)) == set():
                        return num.number

    def find_nine(self):
        possibles = filter(lambda x: len(x.display_string) == 6, self.signal)
        four = self.find_number(4)
        for pos in possibles:
            if set(four).difference(set(pos.display_string)) == set():
                pos.number = 9

    def find_six(self):
        possibles = filter(lambda x: len(x.display_string) == 6, self.signal)
        one = self.find_number(1)
        for pos in possibles:
            if len(set(one).difference(set(pos.display_string))) == 1:
                pos.number = 6

    def find_five(self):
        possibles = filter(lambda x: len(x.display_string) == 5, self.signal)
        six = self.find_number(6)
        for pos in possibles:
            if len(set(six).difference(set(pos.display_string))) == 1:
                pos.number = 5

    def find_three(self):
        possibles = filter(lambda x: len(x.display_string) == 5, self.signal)
        six = self.find_number(5)
        for pos in possibles:
            if len(set(six).difference(set(pos.display_string))) == 1:
                pos.number = 3

    def find_two(self):
        possibles = filter(lambda x: len(x.display_string) == 5, self.signal)
        six = self.find_number(5)
        for pos in possibles:
            if len(set(six).difference(set(pos.display_string))) == 2:
                pos.number = 2

    def find_zero(self):
        for num in self.signal:
            if num.number is None:
                num.number = 0
