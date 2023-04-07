class Board:
    def __init__(self, deck):
        self.board = [[None, None, None, None], [None, None, None], [None, None, None] ]
        for i in range(3):
            for j in range(len(self.board[i])):
                self.board[i][j] = deck[0]
                deck.pop(0)

    def soft_reset(self, deck):
        for i in range(3):
            for j in range(len(self.board[i])):
                if self.board[i][j] == None:
                    if len(deck) > 0:
                        self.board[i][j] = deck[0]
                        deck.pop(0)
                    else:
                        return False
                else:
                    if len(deck) > 0:
                        self.board[i][j] = deck[0]
                        deck.pop(0)
                    else:
                        return False
                    return
                    

    def update(self,position,card):
        self.board[position[0]][position[1]] = card

    def get(self, position):
        return self.board[position[0]][position[1]]