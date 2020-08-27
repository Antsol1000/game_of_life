import life_game as lg
import tkinter as tk
import settings as sett

root = tk.Tk()
root.title("GAME OF LIFE")
root.iconbitmap(sett.ICON_PATH)

if __name__ == '__main__':

    board = lg.Board(root, 10, "X", "#ff0000")
    board.draw()
    board.show()
    board.show_buttons()

    root.mainloop()
