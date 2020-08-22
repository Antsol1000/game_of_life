import life_game as lg
import tkinter as tk

root = tk.Tk()
root.title("GAME OF LIFE")

board = lg.Board(root, 10, "X")
board.draw()
board.show()
board.show_buttons()

root.mainloop()
