from tkinter import *
from life_game import *
from settings import *
import time

root = Tk()
root.title("GAME OF LIFE")

SIZE = 20
board = Board(root, SIZE, "X")
board.draw()
board.show()

settings_button = Button(root, text="SETTINGS", height=1,
                         command=lambda: settings())
settings_button.grid(columnspan=3, column=SIZE - 3, row=0)

start_game_button = Button(root, text="START", height=1,
                           command=lambda b=board: b.start_game())
start_game_button.grid(columnspan=3, column=0, row=SIZE + 1)
step_button = Button(root, text="STEP", height=1,
                     command=lambda b=board: b.step())
step_button.grid(columnspan=3, column=SIZE // 2 - 1, row=SIZE + 1)
draw_button = Button(root, text='DRAW', height=1,
                     command=lambda b=board: b.draw())
draw_button.grid(columnspan=3, column=SIZE - 3, row=SIZE + 1)

root.mainloop()
