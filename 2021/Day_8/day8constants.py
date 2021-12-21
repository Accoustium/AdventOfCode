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

    def __repr__(self):
        return f"Display({''.join(map(lambda x: str(x.number), self.signal))} | {''.join(map(lambda x: str(x.number), self.output))})"

    def find_eight(self) -> str:
        for num in self.signal:
            if num.number == 8:
                return num.display_string
