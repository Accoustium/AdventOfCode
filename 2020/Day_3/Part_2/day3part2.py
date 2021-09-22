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
    trees = {
        0: {'count': 0, 'step': (1, 1)},
        1: {'count': 0, 'step': (3, 1)},
        2: {'count': 0, 'step': (5, 1)},
        3: {'count': 0, 'step': (7, 1)},
        4: {'count': 0, 'step': (1, 2)},
    }
    tree = 0

    for idx, mapping in trees.items():
        mp = Map(mapping['step'])
        while mp.current_coords[1] < len(mp.field):
            if mp.is_tree():
                mapping['count'] += 1
            mp.next_step()
        if tree == 0:
            tree = mapping['count']
        else:
            tree *= mapping['count']

    print(f"Number of trees hit: {tree}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
    # Number of trees hit: 1574890240
