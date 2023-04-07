from game import Game
from human_player import HumanPlayer
from ai_player import AIPlayer
import play

import tkinter

window = tkinter.Tk(className="Higher or Lower")
window.mainloop()

player = AIPlayer()
play.multiple_game(player)

