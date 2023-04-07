from game import Game
from human_player import HumanPlayer

def test():
    wins = 0
    weeks = 1000000
    games = 0
    for i in range(weeks):
        result = play_game()
        if result > 0:
            wins += 1
            games += result
        else:
            games += 3

    estimated_win_chance = round((wins / games) * 100, 2)

    print(
        '''
        ---------------- Results ------------------
        In ''' + str(weeks) + ''' weeks with 3 tickets a week there were ''' + str(wins) + ''' wins
        This gives an estimated win probability for any given player of ''' + str(estimated_win_chance) + '''%'''
    )


player = HumanPlayer()
game = Game()
game.play(player)
