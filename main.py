from game import Game
from human_player import HumanPlayer
from ai_player import AIPlayer
import play

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


def button_click(value):
    if value == 1:
        print("higher")
    else:
        print("Lower")

class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)


        # set window title
        master.title("Higher or Lower")

        # add message to window
        message = tk.Label(master, text="Higher or Lower")
        message.grid()

        # set window size
        window_width = 800
        window_height = 600

        # get the screen dimensions
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        master.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # set the window to be non resizable
        master.resizable(False,False)

        # icon
        master.iconbitmap("./assets/joker.ico")

        

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=0, column=0)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=0, column=1)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=0, column=2)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=0, column=3)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=1, column=1)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=1, column=2)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=1, column=3)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=2, column=1)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=2, column=2)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=2, column=3)

        ttk.Button(master, text="Higher", command=lambda: button_click(1)).grid()
        ttk.Button(master, text="Lower", command=lambda: button_click(0)).grid()
        ttk.Button(master, text="Swap").grid()



root = tk.Tk()
app = GUI(master=root)
app.mainloop()
root.destroy()

#player = AIPlayer()
#play.multiple_game(player)

