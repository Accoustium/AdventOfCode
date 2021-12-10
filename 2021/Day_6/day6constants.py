from typing import *


class LanturnFish:
    def __init__(self, reproduce: int = 8):
        self.day = reproduce

    def next_day(self) -> bool:
        """
        Subtracts a day until it reproduces.  If < 0 resets to 6
        and returns True to create new fish.
        """
        self.day -= 1

        if self.day < 0:
            self.day = 6
            return True
        else:
            return False
