from player import Player
from results import Results

class HumanPlayer(Player):
    def __init__(self):
        self.results = Results()

    def swap(self, card, board):
        swap = input("Enter y to swap card: ")
        if swap == "y":
            return 1
        else:
            return -1
        
    def lose(self):
        print("Sorry, you lost")

    def win(self):
        print("Congratulations, you won")

    def choose(self, card, board):
        choice = int(input("Enter 1 for higher and 0 for lower: "))
        return choice