import tkinter as tk
import random
import settings


class Board:
    """
    class Board,
    """

    def __init__(self, root, size, char):
        self.settings_button = tk.Button(root, text="SETTINGS", height=1,
                                         command=lambda: settings.start(self))
        self.exit_button = tk.Button(root, text="EXIT", height=1,
                                     command=root.destroy)
        self.draw_button = tk.Button(root, text='DRAW', height=1,
                                     command=self.draw)
        self.start_game_button = tk.Button(root, text="START", height=1,
                                           command=lambda: self.start_game(settings.TIME_STEP))
        self.step_count = 0
        self.char = char
        self.size = size
        self.root = root
        self.board = [[tk.Button(root, width=2, height=1,
                                 command=lambda r=j, c=i: self.click(r, c))
                       for i in range(size)] for j in range(size)]
        self.bin_board = [[0 for i in range(size + 2)] for j in range(size + 2)]

    def show_buttons(self):
        self.settings_button.grid(columnspan=3, column=0, row=0, stick=tk.W)
        self.exit_button.grid(columnspan=3, column=self.size - 3, row=0, stick=tk.E)
        self.draw_button.grid(columnspan=3, column=self.size - 3, row=self.size + 1, stick=tk.E)
        self.start_game_button.grid(columnspan=3, column=0, row=self.size + 1, stick=tk.W)

    def click(self, row, column):
        self.board[row][column]['state'] = tk.DISABLED
        self.board[row][column]['text'] = self.char
        self.bin_board[row + 1][column + 1] = 1

    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j].grid(row=i + 1, column=j)
        tk.Label(self.root, text="day: {}".format(self.step_count)).grid(columnspan=3, column=3,
                                                                         row=0, stick=tk.W)

    def check_status(self, row, column):
        neighbours = self.bin_board[row - 1][column - 1] + self.bin_board[row - 1][column] + \
                     + self.bin_board[row - 1][column + 1] + self.bin_board[row][column - 1] + \
                     + self.bin_board[row][column + 1] + self.bin_board[row + 1][column - 1] + \
                     + self.bin_board[row + 1][column] + self.bin_board[row + 1][column + 1]
        return neighbours

    def start_game(self, time_step):
        self.step(time_step)

    def step(self, time_step):
        self.step_count += 1
        tk.Label(self.root, text="day: {}".format(self.step_count)).grid(columnspan=2, column=3,
                                                                         row=0, stick=tk.W)
        new_bin_board = [x[:] for x in self.bin_board]

        for i in range(self.size):
            for j in range(self.size):
                neighbours = self.check_status(i + 1, j + 1)
                if neighbours == 2:
                    continue
                elif neighbours == 3:
                    new_bin_board[i + 1][j + 1] = 1
                else:
                    new_bin_board[i + 1][j + 1] = 0

        if new_bin_board != self.bin_board:
            self.bin_board = [x[:] for x in new_bin_board]

            for i in range(self.size):
                for j in range(self.size):
                    if self.bin_board[i + 1][j + 1] == 1:
                        self.board[i][j]['text'] = self.char
                    else:
                        self.board[i][j]['text'] = ""

            self.count()
            self.root.after(time_step, lambda: self.step(time_step))

    def draw(self):
        self.clear()
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j]['state'] = tk.DISABLED
                if random.randint(0, 1) == 1:
                    self.click(i, j)
        self.count()

    def clear(self):
        self.bin_board = [[0 for i in range(self.size + 2)] for j in range(self.size + 2)]
        for buttons in self.board:
            for button in buttons:
                button['text'] = ""

    def count(self):
        living_cells = 0
        for i in self.bin_board:
            for j in i:
                living_cells += j
        tk.Label(self.root, text="living cells: {}  ".format(living_cells)).grid(columnspan=4, column=5,
                                                                                 row=0, stick=tk.W)
