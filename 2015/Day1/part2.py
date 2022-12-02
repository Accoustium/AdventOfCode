def read_data():
    with open("data.txt", "r") as f:
        for new_line in f:
            for loc, char in enumerate(new_line):
                yield loc + 1, char


def main():
    level = 0
    for position, character in read_data():
        if character == ")":
            level -= 1
        if character == "(":
            level += 1
        if level == -1:
            print(position)
            break


if __name__ == "__main__":
    main()
