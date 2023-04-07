from card import Card
from board import Board

class Display_Board(Board):
    def __init__(self):
        self.board = [[Card("Blank"), Card("Blank"), Card("Blank"), Card("Blank")],
            [Card("Blank"), Card("Blank"), Card("Blank")],
            [Card("Blank"), Card("Blank"), Card("Blank")]]
        
    def print(self):
        print(self.board[0][0].name + "\t" + self.board[0][1].name + "\t"+ self.board[0][2].name + "\t" + self.board[0][3].name)
        print("\t" + self.board[1][0].name + "\t" + self.board[1][1].name + "\t"+ self.board[1][2].name)
        print("\t" + self.board[2][0].name + "\t" + self.board[2][1].name + "\t"+ self.board[2][2].name)

    def update(self,position,card):
        super().update(position,card)