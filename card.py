class Card:
    def __init__(self, card):
        self.name = card
        if card.isnumeric():
            self.value = int(card)
        else:
            if card == "jack":
                self.value = 11
            elif card == "queen":
                self.value = 12
            elif card == "king":
                self.value = 13
            elif card == "ace":
                self.value = 14
            else:
                self.value = -1
    
    def higher(self, card):
        return self.value < card.value

    def lower(self, card):
        return self.value > card.value 