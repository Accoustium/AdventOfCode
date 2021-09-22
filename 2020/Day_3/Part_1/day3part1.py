from typing import *


class Map:
    def __init__(self, steps: tuple):
        self.current_coords: list = [0, 0]
        self.steps: tuple = steps
        self.field: Union[List[List]] = []
        self.__build_map()

    def is_tree(self) -> bool:
        try:
            return self.field[self.current_coords[1]][self.__clean_x(self.current_coords[0])] == "#"
        except IndexError:
            print(self.current_coords)

    def __clean_x(self, x_coord: int) -> int:
        return x_coord % len(self.field[0])

    def __build_map(self):
        for map_line in read_data_csv('../data.csv'):
            self.field.append(map_line)

    def next_step(self):
        self.current_coords[0] += self.steps[0]
        self.current_coords[1] += self.steps[1]


def read_data_csv(file_name: str) -> Generator:
    with open(file_name, 'r') as file:
        for line in file:
            yield line.strip()


def main() -> int:
    mp = Map((3, 1))
    trees = 0

    while mp.current_coords[1] < len(mp.field):
        if mp.is_tree():
            trees += 1
        mp.next_step()

    print(f"Number of trees hit: {trees}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
    # Number of trees hit: 209
