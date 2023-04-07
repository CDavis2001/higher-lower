from gui_game import Game
import copy

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

        self.master = master
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

        self.board = []
        self.board.append([])

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=0, column=0)
        self.board[0].append(label)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=0, column=1)
        self.board[0].append(label)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=0, column=2)
        self.board[0].append(label)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=0, column=3)
        self.board[0].append(label)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=1, column=0)
        self.board.append([])
        self.board[1].append(label)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=1, column=1)
        self.board[1].append(label)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=1, column=2)
        self.board[1].append(label)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=2, column=0)
        self.board.append([])
        self.board[2].append(label)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=2, column=1)
        self.board[2].append(label)

        image = Image.open("./assets/joker.png")
        image = image.resize((100, 100))
        photo = ImageTk.PhotoImage(image)
        label = ttk.Label(image=photo)
        label.image = photo # this line need to prevent gc
        label.grid(row=2, column=2)
        self.board[2].append(label)

        ttk.Button(master, text="Higher", command=lambda: self.choice.set(1)).grid(row=3, column=1)
        ttk.Button(master, text="Lower", command=lambda: self.choice.set(0)).grid(row=3, column=2)
        ttk.Button(master, text="Swap", command=lambda: self.swap.set(1)).grid(row=4, column=1)
        ttk.Button(master, text="Keep", command=lambda: self.swap.set(0)).grid(row=4, column=2)
        ttk.Button(master, text="Start", command=lambda: self.start()).grid(row=5, column=2)

        self.swap = tk.IntVar()
        self.choice = tk.IntVar()
        
        self.info = ttk.Label(master, text="Information")
        self.info.grid(row=6, column=2)

    def start(self):
        self.game = Game()
        for i in range(3):
            for j in range(len(self.board[i])):
                image = Image.open("./assets/joker.png")
                image = image.resize((100,100))
                photo = ImageTk.PhotoImage(image)
                self.board[i][j].image = photo
                self.board[i][j].configure(image=photo)

        self.play()
        

    def show(self, position, card):
        image = Image.open("./assets/" + card.name + card.suit + ".png")
        image = image.resize((100,100))
        photo = ImageTk.PhotoImage(image)
        self.board[position[0]][position[1]].image = photo
        self.board[position[0]][position[1]].configure(image=photo)

    def play(self):
        place = 1
        while place < 10:
            position = self.game.translate(place-1)
            card = copy.copy(self.game.board.get(position))
            next_position = self.game.translate(place)
            next_card = copy.copy(self.game.board.get(next_position))
            self.show(position, card)
            if position == [0,4] or position == [0,0]:
                self.info.configure(text="Swap or Keep")
                self.master.wait_variable(self.swap)
                if self.swap.get() == 1:
                    card = self.game.swap_card(position)
                    self.show(position, card)
                    
            self.game.board.update(position, None)
            self.info.configure(text="Higher or Lower")
            self.master.wait_variable(self.choice)

            if self.choice.get() == 1:
                if not card.higher(next_card):
                    self.info.configure(text="Sorry, you lose")
                    self.show(next_position, next_card)
                    return
            else:
                if not card.lower(next_card):
                    self.info.configure(text="Sorry, you lose")
                    self.show(next_position, next_card)
                    return
                
            card = copy.copy(next_card)
            place += 1
        self.info.configure(text="Congratulations")
        return

root = tk.Tk()
app = GUI(master=root)
app.mainloop()
app.destroy()

#player = AIPlayer()
#play.multiple_game(player)

