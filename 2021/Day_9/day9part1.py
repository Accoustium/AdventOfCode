from day9constants import Map


def main() -> int:
    risk_level = 0
    m = Map()
    for y, level in enumerate(m.map):
        for x in range(len(level)):
            if m.is_low_point(x, y):
                risk_level += m.map[y][x] + 1

    print(risk_level)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
