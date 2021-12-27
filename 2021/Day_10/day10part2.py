from day10constants import generate_chunk, Chunk


def main() -> int:
    incomplete = list()
    for line in generate_chunk():
        c = Chunk(line)
        if c.incomplete:
            incomplete.append(c.points)

    incomplete.sort()
    print(incomplete[len(incomplete) // 2])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
