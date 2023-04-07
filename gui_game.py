import copy
import random
from card import Card
from board import Board



class Game:
    def __init__(self):
        self.make_deck()
        self.board = Board(self.deck)
        

    def make_deck(self):
        suits = ["clubs", "hearts", "diamonds", "spades"]
        self.deck = []
        types = ["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
        for value in types:
            for i in range(4):
                self.deck.append(Card(value, suits[i]))
        random.shuffle(self.deck)
        

    def translate(self, index):
        if index < 4:
            return [0,index]
        if index < 7:
            return [1,index-4]
        if index < 10:
            return [2,index- 7]

    def swap_card(self, position):
        card = copy.copy(self.deck[0])
        self.deck.pop(0)
        return card

    