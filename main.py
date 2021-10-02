import math as math
import numpy as np
import random


class Wheel:
    def __init__(self, x=None):
        self.land = x

    def val(self):
        self.land = random.randint(-1, 37)


def main():
    ask()
    tell()


def ask():
    money = float(input("How Much money are you bringing to the Table? (dollar amount): $"))
    print(f"You have brought ${money:.0f} to the table.")

    def _ask2():
        _ok = str(input("Type 'Ok' to continue or 'quit' to quit: ").lower())
        if _ok == "ok":
            print("\nPayouts:")
            print("Single number bet pays 35 to 1")
            print("Double number bet pays 17 to 1")
            print("Three number bet pays 11 to 1")
            print("Four number bet pays 8 to 1")
            print("Five number bet pays 6 to 1")
            print("Six number bet pays 5 to 1")
            print("Dozens pays 2 to 1")
            print("Column bets pays 2 to 1")
            print("1-18 pays even money")
            print("19-36 pays even money")
            print("Red or black pays even money")
            print("Odd or even bets pays even money\n")
            pass
        elif _ok == "quit":
            _kill()
        else:
            _ask2()
    _ask2()


def tell():
    g = input("Type anything to get value and 'quit' to quit: ").lower()
    if g == 'quit':
        _kill()
    else:
        print(f"{Wheel.land}")
        tell()

def _kill():
    exit()


if __name__ == '__main__':
    main()

