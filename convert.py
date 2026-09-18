import argparse

from temperature import c_to_f, c_to_k, f_to_c


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("value", type=float)
    parser.add_argument("--to", choices=("f", "c", "k"), required=True)
    args = parser.parse_args(argv)

    conversions = {
        "f": c_to_f,
        "c": f_to_c,
        "k": c_to_k,
    }

    try:
        result = conversions[args.to](args.value)
    except ValueError as error:
        print(f"error: {error}")
        return 1

    print(round(result, 2))
    return 0


if __name__ == "__main__":
    main()
