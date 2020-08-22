from tkinter import *
from life_game import *
from settings import *
import time

root = Tk()
root.title("GAME OF LIFE")

SIZE = 20
CHAR = "X"
TIME_STEP = 500


def settings():
    sett = Settings()


board = Board(root, SIZE, CHAR)

board.draw()
board.show()

settings_button = Button(root, text="SETTINGS", height=1,
                         command=settings)
settings_button.grid(columnspan=3, column=0, row=0, stick=W)

exit_button = Button(root, text="EXIT", height=1,
                     command=root.destroy)
exit_button.grid(columnspan=3, column=SIZE - 3, row=0, stick=E)

draw_button = Button(root, text='DRAW', height=1,
                     command=board.draw)
draw_button.grid(columnspan=3, column=SIZE - 3, row=SIZE + 1, stick=E)

start_game_button = Button(root, text="START", height=1,
                           command=lambda b=board: b.start_game(TIME_STEP))
start_game_button.grid(columnspan=3, column=0, row=SIZE + 1, stick=W)

root.mainloop()
