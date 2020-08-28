import tkinter as tk
import tkinter.font as font
import random
import settings

""" Relative path to button icons """
SETTINGS_ICON_PATH = "bin\\settings_icon.png"
EXIT_ICON_PATH = "bin\\exit_icon.png"
START_ICON_PATH = "bin\\start_icon.png"
DRAW_ICON_PATH = "bin\\draw_icon.png"
CHOOSE_1_ICON_PATH = "bin\\choose_1_icon.png"
CHOOSE_2_ICON_PATH = "bin\\choose_2_icon.png"
RESET_ICON_PATH = "bin\\reset_icon.png"
CLEAR_ICON_PATH = "bin\\clear_icon.png"


class Board:
    """
    class Board contains all the stuff displayed on root window
    """

    def __init__(self, root, size, char, color):
        """
        constructor creates buttons, board which is call out
        and bin_which is binary representation of the board
        :param root: master window
        :param size: size of the board in cells
        :param char: marks living cell
        """
        # keep icons in class to protect from deleting
        self.settings_image = tk.PhotoImage(file=SETTINGS_ICON_PATH)
        self.exit_image = tk.PhotoImage(file=EXIT_ICON_PATH)
        self.start_image = tk.PhotoImage(file=START_ICON_PATH)
        self.draw_image = tk.PhotoImage(file=DRAW_ICON_PATH)
        self.choose_1_image = tk.PhotoImage(file=CHOOSE_1_ICON_PATH)
        self.choose_2_image = tk.PhotoImage(file=CHOOSE_2_ICON_PATH)
        self.reset_image = tk.PhotoImage(file=RESET_ICON_PATH)
        self.clear_image = tk.PhotoImage(file=CLEAR_ICON_PATH)

        # initialization of functional buttons
        self.settings_button = tk.Button(root, image=self.settings_image,
                                         command=lambda: settings.start(self))
        self.exit_button = tk.Button(root, image=self.exit_image,
                                     command=root.destroy)
        self.start_game_button = tk.Button(root, image=self.start_image,
                                           command=lambda: self.start_game(settings.TIME_STEP))
        self.draw_button = tk.Button(root, image=self.draw_image,
                                     command=self.draw)
        self.choose_button = tk.Button(root, image=self.choose_1_image, text="CHOOSE",
                                       command=self.choose)
        self.reset_day_button = tk.Button(root, image=self.reset_image,
                                          command=self.reset_day)
        self.clear_button = tk.Button(root, image=self.clear_image,
                                      command=self.clear)
        # number of the day
        self.day_number = 0
        # params
        self.char = char
        self.size = size
        self.root = root
        self.color = color
        # initialization of board and its binary representation
        self.board, self.bin_board = None, None
        self.board_init()

    def board_init(self):
        """
        initialization of board and its binary representation
        """
        self.board = [[tk.Button(self.root, width=2, height=1,
                                 disabledforeground=self.color, font=font.Font(size=10, weight='bold'),
                                 command=lambda row=j, column=i: self.click_cell(row, column))
                       for i in range(self.size)] for j in range(self.size)]
        self.bin_board = [[0 for i in range(self.size + 2)] for j in range(self.size + 2)]

    def show_buttons(self):
        """
        display functional buttons
        """
        # top
        self.settings_button.grid(columnspan=2, column=0, row=0, stick=tk.W)
        self.exit_button.grid(columnspan=2, column=self.size - 2, row=0, stick=tk.E)
        # bottom left
        self.start_game_button.grid(columnspan=2, column=0, row=self.size + 1, stick=tk.W)
        self.draw_button.grid(columnspan=2, column=2, row=self.size + 1)
        self.choose_button.grid(columnspan=2, column=4, row=self.size + 1)
        # bottom right
        self.clear_button.grid(columnspan=2, column=self.size - 2, row=self.size + 1, stick=tk.E)
        self.reset_day_button.grid(columnspan=2, column=self.size - 4, row=self.size + 1)

    def wake_cell(self, row, column):
        """
        come alive cell in row and column given in params
        """
        self.board[row][column]['state'] = tk.DISABLED
        self.board[row][column]['text'] = self.char
        self.bin_board[row + 1][column + 1] = 1

    def click_cell(self, row, column):
        """
        change the status of cell
        """
        if self.board[row][column]['text'] == "":
            self.board[row][column]['text'] = self.char
            self.bin_board[row + 1][column + 1] = 1
        else:
            self.board[row][column]['text'] = ""
            self.bin_board[row + 1][column + 1] = 0

    def choose(self):
        """
        enable to manually change the state of cell
        """
        if self.choose_button['text'] == "CHOOSE":
            for buttons in self.board:
                for button in buttons:
                    button['state'] = tk.NORMAL
            self.choose_button['image'] = self.choose_2_image
            self.choose_button['text'] = "SAVE"
            self.start_game_button['state'] = tk.DISABLED
            self.draw_button['state'] = tk.DISABLED
        else:
            for buttons in self.board:
                for button in buttons:
                    button['state'] = tk.DISABLED
            self.choose_button['image'] = self.choose_1_image
            self.choose_button['text'] = "CHOOSE"
            self.start_game_button['state'] = tk.NORMAL
            self.draw_button['state'] = tk.NORMAL

    def show(self):
        """
        display the board
        """
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j].grid(row=i + 1, column=j)
        self.show_day_number()
        self.show_number_of_living_cells()

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
        self.day_number += 1
        self.show_day_number()
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
        # and program should stop making start_game_button DISABLED
        if new_bin_board != self.bin_board:
            self.bin_board = [x[:] for x in new_bin_board]

            for i in range(self.size):
                for j in range(self.size):
                    if self.bin_board[i + 1][j + 1] == 1:
                        self.board[i][j]['text'] = self.char
                    else:
                        self.board[i][j]['text'] = ""

            # count alive cells and call out next step() after TIME_STEP
            self.show_number_of_living_cells()
            self.root.after(time_step, lambda: self.step(time_step))
        else:
            self.start_game_button['state'] = tk.DISABLED

    def draw(self):
        """
        draw alive cells in the beginning
        """
        self.clear()
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j]['state'] = tk.DISABLED
                if random.randint(0, 1) == 1:
                    self.wake_cell(i, j)
        self.show_number_of_living_cells()
        self.start_game_button['state'] = tk.NORMAL

    def clear(self):
        """
        clear the board from alive cells
        """
        self.bin_board = [[0 for i in range(self.size + 2)] for j in range(self.size + 2)]
        for buttons in self.board:
            for button in buttons:
                button['text'] = ""
        self.show_number_of_living_cells()

    def count_living_cells(self):
        """
        :return: number of living cells
        """
        living_cells = 0
        for i in self.bin_board:
            for j in i:
                living_cells += j
        return living_cells

    def show_number_of_living_cells(self):
        """
        display number of living cells
        """
        tk.Label(self.root,
                 text="living cells: {}  ".format(self.count_living_cells())).grid(columnspan=4, column=5,
                                                                                   row=0, stick=tk.W)

    def reset_day(self):
        """
        reset and display day_number
        """
        self.day_number = 0
        self.show_day_number()

    def show_day_number(self):
        """
        display label with day_number
        """
        tk.Label(self.root, text="day:{:03d}".format(self.day_number)).grid(columnspan=2, column=2,
                                                                            row=0, stick=tk.W)
