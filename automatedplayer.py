import random

from dice_settings import Dice

class AutomatedPlayer:

    def __init(self, cpu: bool, initial_bank: float):
        self.dice = None
        self.bet_amount = None
        self.wins = 0
        self.loses = 0
        self.cpu = cpu
        self.bank = initial_bank

    def throw_dice(self):
        self.dice = Dice.throw_dice()

    def bet(self, bet_amount, minimum_amount = 1):
        if self.cpu:
            bet_amount = random.randint(minimum_amount, int(self.bank))
        else:

            match self.dice:
                case 1:
                    self.bet_amount = 0.1 * self.bank
                case 2:
                    self.bet_amount = 0.2 * self.bank
                case 3:
                    self.bet_amount = 0.3 * self.bank
                case 4:
                    self.bet_amount = 0.4 * self.bank
                case 5:
                    self.bet_amount = 0.5 * self.bank
                case 6:
                    self.bet_amount = self.bank

    def win(self, amount):
        self.bank += amount - self.bet_amount
        self.wins += 1
        if not self.cpu:
            print(f"You win ${self.bet_amount} and your bank is ${self.bank}")
        self.bet_amount = 0

    def lose(self):
        self.bank -= self.bet_amount
        if not self.cpu:
            print(f"You lost ${self.bet_amount} and your bank is ${self.bank}")
        self.bet_amount = 0

