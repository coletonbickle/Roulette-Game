# import math as math
# import numpy as np
import random


class Wheel:
    def __init__(self, bet, loc, x=0):
        self.bet = bet
        self.loc = loc
        self.land = x
        self.color = None
        self.evens = None
        self.lows = None
        self.dozens = None
        self.columns = None

    def val(self):
        self.land = random.randint(-1, 37)
        # Create conditionals here to see if bet location matches table outcome

    def output(self):
        if self.land != (0 or -1):
            # Checks if landed value is red or black
            num = [1, 2, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
            if self.land in num:
                self.color = 'red'
            else:
                self.color = 'black'

            # Checks if landed value is even or odd
            if (self.land % 2) == 0:
                self.evens = 'even'
            else:
                self.evens = 'odd'

            # Checks if landed value is high or low
            if self.land < 19:
                self.lows = 'low'
            else:
                self.lows = 'high'

            # Checks which dozen landed value is in
            if self.land in range(1, 12):
                self.dozens = 'first'
            elif self.land in range(13, 24):
                self.dozens = 'second'
            else:
                self.dozens = 'third'

            # Checks which column landed value is in
            if (self.land % 3) == 1:
                self.columns = 'col1'
            elif (self.land % 3) == 2:
                self.columns = 'col2'
            else:
                self.columns = 'col3'


class Player:
    def __init__(self, x=0, y=None):
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
            _payout()
            break
        elif _ok == "quit":
            _kill()


def _payout():
    print("\nPayouts:")
    print("Input 'single' - Single number bet pays 35 to 1")
    print("Input 'double' - Double number bet pays 17 to 1")
    print("Input 'triple' - Three number bet pays 11 to 1")
    print("Input 'four' - Four number bet pays 8 to 1")
    print("Input 'five' - Five number bet pays 6 to 1")
    print("Input 'six' - Six number bet pays 5 to 1")
    print("Input 'dozen' - Dozens pays 2 to 1")
    print("Input 'column' - Column bets pays 2 to 1")
    print("Input 'half' - 1-18 pays even money")
    print("Input 'half' - 19-36 pays even money")
    print("Input 'red' or 'black' - Red or black pays even money")
    print("Input 'odd' or 'even' - Odd or even bets pays even money\n")

def _bet():
    print("How much do you want to bet and where do you want it?")
    print("Type 'payouts' to display all payouts")
    while Player.loc is None:  # Fix issue here
        Player.loc = str(input("Type where you would like to place your bet:\n")).lower()
        if Player.loc == "payouts":
            _payout()
            Player.loc = None
        elif Player.loc == "single" or "double" or "triple" or "four" or "five" or "six" or "dozen" or "column" or \
                "half" or "red" or "black" or "even" or "odd":
            break
        else:
            Player.loc = None

    Player.bet = input(f"(${Player.money} remaining)How much would you like to bet? \n$")
    print(f"\nyou have place ${Player.bet} on {Player.loc}")


def _kill():
    exit()


if __name__ == '__main__':
    main()

