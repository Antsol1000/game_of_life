import tkinter as tk

TIME_STEP = 500


def start(board):
    s = Settings(board)


class Settings:

    def __init__(self, board):
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
        tk.Label(self.top, text="CHAR: ").grid(row=0, column=0, stick=tk.W)
        self.char_entry.grid(row=0, column=1)
        tk.Label(self.top, text="SIZE: ").grid(row=1, column=0, stick=tk.W)
        self.size_entry.grid(row=1, column=1)
        tk.Label(self.top, text="TIME STEP [ms]: ").grid(row=2, column=0, stick=tk.W)
        self.time_step_entry.grid(row=2, column=1)

        self.save_button.grid(row=3, columnspan=2)

    def set_char(self, board):
        board.char = self.char_entry.get()

    def set_size(self, board):
        board.size = int(self.size_entry.get())

    def set_time_step(self):
        global TIME_STEP
        TIME_STEP = int(self.time_step_entry.get())

    def save_settings(self, board):
        self.set_char(board)
        self.set_size(board)
        self.set_time_step()
        board.board = [[tk.Button(board.root, width=2, height=1,
                                  command=lambda r=j, c=i: board.click(r, c))
                       for i in range(board.size)] for j in range(board.size)]
        board.bin_board = [[0 for i in range(board.size + 2)] for j in range(board.size + 2)]
        board.draw()
        board.show()
        board.show_buttons()
        self.top.destroy()