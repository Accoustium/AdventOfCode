class Elf:
    def __init__(self, calories: list):
        self.calorie_list = calories

    def __repr__(self):
        return f"Elf({self.calories})"

    def __str__(self):
        return str(self.__repr__())

    def __int__(self):
        return self.calories

    @property
    def calories(self):
        return sum(self.calorie_list)

    def __gt__(self, other):
        if self.calories > other.calories:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.calories < other.calories:
            return True
        else:
            return False


def read_calories_packs():
    with open("data.txt", "r") as f:
        for new_line in f:
            yield new_line


def main():
    elfs = []
    calories = []

    for calorie in read_calories_packs():
        if calorie == "\n":
            elfs.append(Elf(calories))
            calories = []
        else:
            calories.append(int(calorie))

    elfs.sort(key=lambda x: x.calories, reverse=True)
    print(sum(map(lambda x: int(x), elfs[:3])))



if __name__ == "__main__":
    main()