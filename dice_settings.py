import random


class Dice:
    def __init__(self, dice_sides: int, dice_number: int):
        self.dice = None
        self.dice_sides = dice_sides
        self.dice_number = dice_number

    def throw_dice(self):
        self.dice = sum([random.randint(1, self.dice_sides) for _ in range(self.dice_number)])
        return self.dice

