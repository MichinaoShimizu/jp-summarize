import sys

from src.processor import SumyActionProcessor


def main() -> int:
    [print(text) for text in SumyActionProcessor(sys.stdin.readline()).run()]
    return 0


if __name__ == "__main__":
    main()
