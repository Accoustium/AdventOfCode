def read_data():
    with open("data.txt", "r") as f:
        for new_line in f:
            l, w, h = new_line.split("x")
            yield int(l), int(w), int(h)


def main():
    total = 0
    for l, w, h in read_data():
        smallest_sides = [l, w, h]
        smallest_sides.sort()
        total += (2 * smallest_sides[0] + 2 * smallest_sides[1]) + (l * w * h)

    print(total)


if __name__ == "__main__":
    main()
