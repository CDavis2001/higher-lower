from player import Player
from results import Results


class AIPlayer(Player):
    def __init__(self):
        self.results = Results()

    def swap(self, card, board):
        switch_on = [6,7,8,9]
        if card.value in switch_on:
            return 1
        return 0

    def lose(self):
        self.results.games += 1

    def win(self):
        self.results.games += 1
        self.results.wins += 1

    def choose(self, card, board):
        if card.value < 8:
            return 1
        return -1