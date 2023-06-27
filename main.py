# Two players at least
# Each of them has a bank
# Throw dice
# Bet
# Win/Lose

import random


class Player:
    def __init__(self, cpu: bool, initial_bank: float, dice_sides: int, dice_number: int):
        # TODO: Add dice class
        self.dice = None
        self.dice_sides = dice_sides
        self.dice_number = dice_number
        self.wins = 0
        self.bet_amount = None
        self.bank = initial_bank
        self.cpu = cpu

    def throw_dice(self):
        self.dice = sum([random.randint(1, self.dice_sides) for _ in range(self.dice_number)])

    def bet(self, bet_amount=None, minimum_amount=1):
        # TODO: Simulate different strategy
        if not self.cpu:
            self.bet_amount = bet_amount
        else:
            self.bet_amount = random.randint(minimum_amount, int(self.bank))

    def win(self, amount):
        self.bank += amount - self.bet_amount
        self.wins += 1
        if not self.cpu:
            print(f"You win ${amount}. Bank is ${self.bank}")
        self.bet_amount = 0

    def lose(self):
        self.bank -= self.bet_amount
        if not self.cpu:
            print(f"You lose ${self.bet_amount}. Bank is ${self.bank}")
        self.bet_amount = 0


class Game:
    def __init__(self, num_of_players=2, initial_bank=500.0, rounds=4, dice_sides=6, dice_number=1):
        self.dice_number = dice_number
        self.dice_sides = dice_sides
        self.rounds = rounds
        self.players = None
        self.initial_bank = initial_bank
        self.num_of_players = num_of_players
        self.create_players()

    def create_players(self):
        self.players = [
            Player(True, self.initial_bank, self.dice_sides, self.dice_number)
            for _ in range(self.num_of_players - 1)
        ]
        self.players.append(Player(False, self.initial_bank, self.dice_sides, self.dice_number))

    def throw_dices(self):
        players_next_stage = []
        for player in self.players:
            try:
                minimum_bet = random.randint(1, player.bank // 3)
            except:
                print(f"Player has {player.bank} and cannot continue playing ...")
                continue
            player.throw_dice()
            if player.cpu:
                player.bet(minimum_amount=minimum_bet)
            else:
                while True:
                    print(f"Your result is {player.dice}")
                    print(f"Minimum bet is {minimum_bet}")
                    bet_amount = float(input(f"You currently have ${player.bank}: Enter your bet: "))
                    if player.bank >= bet_amount >= minimum_bet:
                        break
                    print(f"You can bet a maximum of ${player.bank} and a minimum of ${minimum_bet}")
                player.bet(bet_amount)

            players_next_stage.append(player)

        self.players = players_next_stage

    def calculate_scores(self):
        dices = [player.dice for player in self.players]
        winning_dice = max([player.dice for player in self.players])
        winners = dices.count(winning_dice)
        print(f"We have {winners} winners!")
        amount = sum([player.bet_amount for player in self.players]) / winners
        players_next_stage = []
        for player in self.players:
            if player.dice == winning_dice:
                if player.cpu:
                    print(f"Player CPU has a bet of ${player.bet_amount} won ${amount} with result {player.dice}")
                player.win(amount)
            else:
                if player.cpu:
                    print(f"Player CPU lost ${player.bet_amount} with result {player.dice}")
                player.lose()
            players_next_stage.append(player)

        self.players = players_next_stage

    def run(self):
        for i in range(1, self.rounds + 1):
            print(f"Round {i}")
            self.throw_dices()
            self.calculate_scores()
            print("----------------------------------------")
        for player in self.players:
            name = "CPU" if player.cpu else "Player"
            print(f"{name} has bank amount of {player.bank} and {player.wins} wins.")


if __name__ == "__main__":
    players = int(input("Enter player count: "))
    rounds = int(input("Enter round count: "))
    initial_bank = float(input("Enter initial bank: "))
    dice_number = int(input("Please enter the number of dices: "))
    dice_sides = int(input("Please enter the number of sides for each dice: "))
    game = Game(players, initial_bank, rounds, dice_sides, dice_number)
    game.run()
