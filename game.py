import copy
import random
from card import Card
from board import Board
from display_board import Display_Board

class Game:
    def __init__(self):
        self.make_deck()
        self.board = Board(self.deck)
        self.display_board = Display_Board()

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
        self.display_board.update(position,card)
        return card

    def play(self, player):
        place = 1
        while place < 10:
            # translate linear place to 2d board position
            position = self.translate(place - 1)
            # get current card
            card = copy.copy(self.board.get(position))
            self.display_board.update(position, card)
            next_position = self.translate(place)
            next_card = copy.copy(self.board.get(next_position))
            self.display_board.print()

            if position == [1,0] or position == [0,0]:
                if player.swap(card, self.board) == 1:
                    card = self.swap_card(position)
                    self.display_board.print()
            
            self.board.update(position, None)
            self.display_board.update(next_position, next_card)


            choice = player.choose(card, self.board)

            if choice == 1:
                if not card.higher(next_card):
                    player.lose()
                    return
            else:
                if not card.lower(next_card):

                    player.lose()
                    return
                
            card = copy.copy(next_card)
            place += 1
        player.win()
        return