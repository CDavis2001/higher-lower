class Results:
    def __init__(self):
        self.wins = 0
        self.games = 0

    def reset(self):
        self.wins = 0
        self.games = 0

    def get_win_rate(self):
        win_rate = self.wins / self.games
        return win_rate
    
    def get_percent_win_rate(self):
        win_rate = self.get_win_rate()
        return win_rate * 100