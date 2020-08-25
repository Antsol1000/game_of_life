import tkinter as tk

TIME_STEP = 500


def start(board):
    """
    this function is used to call out Settings window
    """
    s = Settings(board)


class Settings:
    """
    class Settings calls out Settings window
    allows one to change:
    sign which indicate living cell
    size of the board
    TIME_STEP - length of the game's day
    """

    def __init__(self, board):
        """
        creates new window, entries for params and save button param
        at the end it calls self.show() which grids all the stuff
        """
        # creates new window
        self.top = tk.Toplevel()
        self.top.title("SETTINGS")

        # creates entries for params
        self.char_entry = tk.Entry(self.top, width=10)
        self.char_entry.insert(0, 'X')
        self.size_entry = tk.Entry(self.top, width=10)
        self.size_entry.insert(0, '10')
        self.time_step_entry = tk.Entry(self.top, width=10)
        self.time_step_entry.insert(0, '500')

        # creates save_settings button
        self.save_button = tk.Button(self.top, text="SAVE SETTINGS",
                                     command=lambda b=board: self.save_settings(b))

        self.show()

    def show(self):
        """
        grids entries and labels for params
        grids save_button
        """
        tk.Label(self.top, text="CHAR: ").grid(row=0, column=0, stick=tk.W)
        self.char_entry.grid(row=0, column=1)
        tk.Label(self.top, text="SIZE: ").grid(row=1, column=0, stick=tk.W)
        self.size_entry.grid(row=1, column=1)
        tk.Label(self.top, text="TIME STEP [ms]: ").grid(row=2, column=0, stick=tk.W)
        self.time_step_entry.grid(row=2, column=1)

        self.save_button.grid(row=3, columnspan=2)

    def set_char(self, board):
        """
        sets param char, taken from entry
        """
        board.char = self.char_entry.get()

    def set_size(self, board):
        """
        sets param size, taken from entry
        """
        board.size = int(self.size_entry.get())

    def set_time_step(self):
        """
        sets param TIME_STEP, taken from entry
        """
        global TIME_STEP
        TIME_STEP = int(self.time_step_entry.get())

    def save_settings(self, board):
        """
        this function is called when one clicks save_button
        it sets all params, edits the board and destroy Settings window
        """
        # set param
        self.set_char(board)
        self.set_size(board)
        self.set_time_step()

        # edit the board and show new
        board.board = [[tk.Button(board.root, width=2, height=1,
                                  command=lambda r=j, c=i: board.click(r, c))
                        for i in range(board.size)] for j in range(board.size)]
        board.bin_board = [[0 for i in range(board.size + 2)] for j in range(board.size + 2)]
        board.draw()
        board.show()
        board.show_buttons()

        # destroy Settings window
        self.top.destroy()
