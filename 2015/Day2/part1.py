def read_data():
    with open("data.txt", "r") as f:
        for new_line in f:
            l, w, h = new_line.split("x")
            yield int(l), int(w), int(h)


def main():
    total = 0
    for l, w, h in read_data():
        total += ( 2*l*w + 2*w*h + 2*h*l )
        if 2*l*w > 2*w*h:
            if 2*w*h > 2*h*l:
                total += h*l
            else:
                total += w*h
        else:
            if 2*l*w > 2*h*l:
                total += h*l
            else:
                total += l*w

    print(total)


if __name__ == "__main__":
    main()
