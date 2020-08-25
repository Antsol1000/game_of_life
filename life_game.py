import tkinter as tk
import random
import settings


class Board:
    """
    class Board contains all the stuff displayed on root window
    """

    def __init__(self, root, size, char):
        """
        constructor creates buttons, board which is call out
        and bin_which is binary representation of the board
        :param root: master window
        :param size: size of the board in cells
        :param char: marks living cell
        """
        # initialization of functional buttons
        self.settings_button = tk.Button(root, text="SETTINGS", height=1,
                                         command=lambda: settings.start(self))
        self.exit_button = tk.Button(root, text="EXIT", height=1,
                                     command=root.destroy)
        self.draw_button = tk.Button(root, text='DRAW', height=1,
                                     command=self.draw)
        self.start_game_button = tk.Button(root, text="START", height=1,
                                           command=lambda: self.start_game(settings.TIME_STEP))
        # number of the day
        self.step_count = 0
        # params
        self.char = char
        self.size = size
        self.root = root
        # initialization of board and its binary representation
        self.board = [[tk.Button(root, width=2, height=1,
                                 command=lambda r=j, c=i: self.click(r, c))
                       for i in range(size)] for j in range(size)]
        self.bin_board = [[0 for i in range(size + 2)] for j in range(size + 2)]

    def show_buttons(self):
        """
        display functional buttons
        """
        self.settings_button.grid(columnspan=3, column=0, row=0, stick=tk.W)
        self.exit_button.grid(columnspan=3, column=self.size - 3, row=0, stick=tk.E)
        self.draw_button.grid(columnspan=3, column=self.size - 3, row=self.size + 1, stick=tk.E)
        self.start_game_button.grid(columnspan=3, column=0, row=self.size + 1, stick=tk.W)

    def click(self, row, column):
        """
        come alive cell in row and column given in params
        """
        self.board[row][column]['state'] = tk.DISABLED
        self.board[row][column]['text'] = self.char
        self.bin_board[row + 1][column + 1] = 1

    def show(self):
        """
        display the board
        """
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j].grid(row=i + 1, column=j)
        tk.Label(self.root, text="day: {}".format(self.step_count)).grid(columnspan=3, column=3,
                                                                         row=0, stick=tk.W)

    def check_status(self, row, column):
        """
        :return: number of alive neighbours
        """
        neighbours = self.bin_board[row - 1][column - 1] + self.bin_board[row - 1][column] + \
                     + self.bin_board[row - 1][column + 1] + self.bin_board[row][column - 1] + \
                     + self.bin_board[row][column + 1] + self.bin_board[row + 1][column - 1] + \
                     + self.bin_board[row + 1][column] + self.bin_board[row + 1][column + 1]
        return neighbours

    def start_game(self, time_step):
        """
        call out first step
        """
        self.step(time_step)

    def step(self, time_step):
        """
        edits the board according to the rules of game
        if game reaches stable composition it stops
        :param time_step: length of the day
        """
        # add 1 to day number
        self.step_count += 1
        tk.Label(self.root, text="day: {}".format(self.step_count)).grid(columnspan=2, column=3,
                                                                         row=0, stick=tk.W)
        # copy the bin board !! remember of copying they are lists!!
        new_bin_board = [x[:] for x in self.bin_board]

        # edit new board
        for i in range(self.size):
            for j in range(self.size):
                neighbours = self.check_status(i + 1, j + 1)
                if neighbours == 2:
                    continue
                elif neighbours == 3:
                    new_bin_board[i + 1][j + 1] = 1
                else:
                    new_bin_board[i + 1][j + 1] = 0

        # if new board is equal to old there is stable format
        # and program should stop
        if new_bin_board != self.bin_board:
            self.bin_board = [x[:] for x in new_bin_board]

            for i in range(self.size):
                for j in range(self.size):
                    if self.bin_board[i + 1][j + 1] == 1:
                        self.board[i][j]['text'] = self.char
                    else:
                        self.board[i][j]['text'] = ""

            # count alive cells and call out next step() after TIME_STEP
            self.count()
            self.root.after(time_step, lambda: self.step(time_step))

    def draw(self):
        """
        draw alive cells in the beginning
        """
        self.clear()
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j]['state'] = tk.DISABLED
                if random.randint(0, 1) == 1:
                    self.click(i, j)
        self.count()

    def clear(self):
        """
        clear the board from alive cells
        """
        self.bin_board = [[0 for i in range(self.size + 2)] for j in range(self.size + 2)]
        for buttons in self.board:
            for button in buttons:
                button['text'] = ""

    def count(self):
        """
        count living cells and display the score
        """
        living_cells = 0
        for i in self.bin_board:
            for j in i:
                living_cells += j
        tk.Label(self.root, text="living cells: {}  ".format(living_cells)).grid(columnspan=4, column=5,
                                                                                 row=0, stick=tk.W)
