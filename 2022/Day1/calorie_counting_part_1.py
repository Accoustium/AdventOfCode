class Elf:
    def __init__(self, calories: list):
        self.calorie_list = calories

    def __repr__(self):
        return f"Elf({self.calorie_list})"

    def __str__(self):
        return str(self.__repr__())

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
    most_elf = Elf([])
    calories = []

    for calorie in read_calories_packs():
        if calorie == "\n":
            elf = Elf(calories)
            if elf > most_elf:
                most_elf = elf
            calories = []
        else:
            calories.append(int(calorie))

    print(most_elf.calories)


if __name__ == "__main__":
    main()
