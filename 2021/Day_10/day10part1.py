from day10constants import generate_chunk, Chunk


def main() -> int:
    total = 0
    for line in generate_chunk():
        c = Chunk(line)
        if c.points != 0:
            total += c.points

    print(total)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
