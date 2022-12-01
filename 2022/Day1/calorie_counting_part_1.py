class Elf:
    def __init__(self, calories: list):
        self.calorie_list = calories

    @property
    def calories(self):
        return sum(self.calorie_list)


def read_calories_packs():
