from game import Game
from ai_player import AIPlayer

def multiple_game(player):
    games = int(input("Enter number of games: "))

    for i in range(games):
        game = Game()
        game.play(player)

    win_rate = round(player.results.get_percent_win_rate(), 2)


    print("In " + str(games) + " games, the player had a win rate of " + str(win_rate))

def game(player):
    game = Game()
    game.play(player)