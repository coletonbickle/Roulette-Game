import math as math
import numpy as np
import random


class Wheel:
    def __init__(self, bet, loc, x=0):
        self.bet = bet
        self.loc = loc
        self.land = x

    def val(self):
        self.land = random.randint(-1, 37)
        # Create conditionals here to see if bet location matches table outcome


class Player:
    def __init__(self, x=0, y=''):
        self.money = x
        self.bet = x
        self.loc = y


def main():
    ask()
    _bet()
    outcome = Wheel(Player.bet, Player.loc)
    outcome.val()


def ask():
    Player.money = float(input("How Much money are you bringing to the Table? (dollar amount): $"))
    print(f"You have brought ${Player.money:.0f} to the table.")

    while Player.money is not None:
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
            break
        elif _ok == "quit":
            _kill()


def _bet():
    print("How much do you want to bet and where do you want it?")
    Player.loc = str(input("Type where you would like to place your bet:\n"))
    Player.bet = input(f"(${Player.money} remaining)How much would you like to bet? \n$")


def _kill():
    exit()


if __name__ == '__main__':
    main()

