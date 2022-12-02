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
    f = open("data.txt", 'r')

    try:
        while True:
            calories = []
            calorie = f.readline()

            while calorie != "\n":
                if calorie != "":
                    calories.append(int(calorie))
                calorie = f.readline()

            yield Elf(calories)
            continue

    except EOFError:
        f.close()


def main():
    most_elf = Elf([])

    for elf in read_calories_packs():
        if elf > most_elf:
            most_elf = elf

    print(most_elf.calories)


if __name__ == "__main__":
    main()
