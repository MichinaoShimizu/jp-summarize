import sys

from src.processor import SumyActionProcessor


def main() -> int:
    [print(s) for s in SumyActionProcessor(sys.stdin.read()).run()]
    return 0


if __name__ == "__main__":
    main()
