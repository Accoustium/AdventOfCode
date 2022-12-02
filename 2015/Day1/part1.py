def main():
    with open("data.txt", "r") as f:
        for new_line in f:
            up = new_line.count("(")
            down = new_line.count(")")

            print(up - down)


if __name__ == "__main__":
    main()
