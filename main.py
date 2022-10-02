# import math as math
# import numpy as np
import random
import time


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
        self.land = random.randint(-1, 36)
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
            if self.land in range(1, 13):
                self.dozens = 'first'
            elif self.land in range(13, 25):
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
        self.color = None
        self.evens = None
        self.lows = None
        self.dozens = None
        self.columns = None

    def Decider(self):
        if self.loc in ["black", "red"]:
            self.color = self.loc
        elif self.loc in ["even", "odd"]:
            self.evens = self.loc
        elif self.loc in ["low", "high"]:
            self.lows = self.loc
        elif self.loc in ["first", "second", "third"]:
            self.dozens = self.loc
        elif self.loc in ["col1", "col2", "col3"]:
            self.columns = self.loc
    
    def clear(self):
        self.color = None
        self.evens = None
        self.lows = None
        self.dozens = None
        self.columns = None



def main():
    person = Player()
    ask(person)
    while person.money > 0.01:
        _bet(person)
        outcome = Wheel(person.bet, person.loc)
        outcome.val()
        outcome.output()
        person.Decider()
        compare(person,outcome)
        person.clear()
    
    print("\nYou have ran out of money! Tough Luck...\n")
    _kill()
    



def ask(person):
    # person.money = 1000
    person.money = float(input("How Much money are you bringing to the Table? (dollar amount): $"))
    print(f"You have brought ${person.money:.0f} to the table.")
    _payout()
    # while person.money is not None:
    #     _ok = str(input("Type 'Ok' to continue or 'quit' to quit: ").lower())
    #     if _ok == "ok":
    #         _payout()
    #         break
    #     elif _ok == "quit":
    #         _kill()


def _payout():
    print("\nPayouts:")
    print("Input 'single' - Single number bet pays 35 to 1")
    # print("Input 'double' - Double number bet pays 17 to 1")
    # print("Input 'triple' - Three number bet pays 11 to 1")
    # print("Input 'four' - Four number bet pays 8 to 1")
    # print("Input 'five' - Five number bet pays 6 to 1")
    # print("Input 'six' - Six number bet pays 5 to 1")
    print("Input 'dozen' - Dozens pays 2 to 1")
    print("Input 'column' - Column bets pays 2 to 1")
    print("Input 'half' - 1-18 pays even money")
    print("Input 'half' - 19-36 pays even money")
    print("Input 'red' or 'black' - Red or black pays even money")
    print("Input 'odd' or 'even' - Odd or even bets pays even money\n")

def _bet(person):
    person.loc = None
    print(f"(${person.money} remaining) How much do you want to bet and where do you want it?")
    print("Type 'payouts' to display all payouts or 'Quit' to quit out")
    while person.loc is None:  
        person.loc = str(input("Type where you would like to place your bet:\n")).lower()
        if person.loc == "payouts":
            _payout()
            person.loc = None
        elif person.loc == "quit":
            _kill()
        elif person.loc == "single":
            while person.loc == "single":
                temp = int(input(f"Which number are you betting on? \n"))
                if temp in range(-1,36):
                    person.loc = temp

        elif person.loc in ["dozen", "column", "half", "red", "black", "even", "odd"]: #"double" or "triple" or "four" or "five" or "six" or 
            if person.loc == "dozen":
                temp = float(input(f"Which dozen are you betting on?  (1, 2 or 3)\n"))
                if temp == 1:
                    person.loc = "first"
                elif temp == 2:
                    person.loc = "second"
                else:
                    person.loc = "third"

            elif person.loc == "column":
                temp = float(input(f"Which column are you betting on? (1, 2 or 3)\n"))
                if temp == 1:
                    person.loc = "col1"
                elif temp == 2:
                    person.loc = "col2"
                else:
                    person.loc = "col3"

            elif person.loc == "half":
                temp = float(input(f"Which half are you betting on? (1 or 2)\n"))
                if temp == 1:
                    person.loc = "low"
                else:
                    person.loc = "high"
            break
        else:
            person.loc = None


    person.bet = float(input(f"(${person.money} remaining) How much would you like to bet? \n$"))
    person.money = person.money - person.bet
    print(f"\nyou have place ${person.bet} on {person.loc}")

def compare(person,outcome):
    print("Spinning Wheel...\n")
    time.sleep(3)
    print(f"\nBall landed on {outcome.land}")
    time.sleep(0.5)

    if isinstance(person.loc,int) is True:
        if person.loc == outcome.land:
            person.money = person.money + (36 * person.bet)
            print(f"You won! {person.bet} added to your balance\n")
    elif person.color != None:
        if person.color == outcome.color:
            person.money = person.money + (2 * person.bet)
            print(f"You won! {person.bet} added to your balance\n")
    elif person.evens != None:
        if person.evens == outcome.evens:
            person.money = person.money + (2 * person.bet)
            print(f"You won! {person.bet} added to your balance\n")
    elif person.lows != None:
        if person.lows == outcome.lows:
           person.money = person.money + (2 * person.bet)
           print(f"You won! {person.bet} added to your balance\n")
    elif person.dozens != None:
        if person.dozens == outcome.dozens:
           person.money = person.money + (3 * person.bet)
           print(f"You won! {person.bet} added to your balance\n")
    elif person.columns != None:
        if person.columns == outcome.columns:
           person.money = person.money + (3 * person.bet)
           print(f"You won! {person.bet} added to your balance\n")
    else:
        print("You lost, try again!\n")
    

def _kill():
    print("\nThanks for playing!\n")
    exit()


if __name__ == '__main__':
    main()

