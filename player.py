from abc import ABC, abstractmethod

class Player(ABC):
    # return value of 1 if wish to swap
    # return anything else if not
    @abstractmethod
    def swap(self, card, board):
        pass
    
    @abstractmethod
    def lose(self):
        pass

    @abstractmethod
    def win(self):
        pass
    
    # return value of 1 for higher
    # return any other value for lower
    @abstractmethod
    def choose(self, card, board):
        pass