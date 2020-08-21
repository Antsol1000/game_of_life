from tkinter import *
from life_game import *
import time

root = Tk()
root.title("GAME OF LIFE")

SIZE = 10
board = Board(root, SIZE)
board.draw()
board.show()

start_game_button = Button(root, text="START", height=1,
                           command=lambda b=board: b.start_game())
start_game_button.grid(row=SIZE + 1, column=0)
step_button = Button(root, text="STEP", height=1,
                     command=lambda b=board: b.step())
step_button.grid(row=SIZE + 1, column=SIZE-1)
draw_button = Button(root, text='DRAW', height=1,
                     command=lambda b=board: b.draw())
draw_button.grid(row=SIZE + 1, column=SIZE // 2)

root.mainloop()
