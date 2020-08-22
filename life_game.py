from tkinter import *
import random


class Board:

    def __init__(self, root, size, char):
        self.step_count = 0
        self.char = char
        self.size = size
        self.root = root
        self.board = [[Button(root, width=2, height=1,
                              command=lambda r=j, c=i: self.click(r, c))
                       for i in range(size)] for j in range(size)]
        self.bin_board = [[0 for i in range(size + 2)] for j in range(size + 2)]

    def click(self, row, column):
        self.board[row][column]['state'] = DISABLED
        self.board[row][column]['text'] = self.char
        self.bin_board[row + 1][column + 1] = 1

    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j].grid(row=i + 1, column=j)
        Label(self.root, text="step: {}".format(self.step_count)).grid(columnspan=3, column=3,
                                                                       row=0, stick=W)

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
        new_bin_board = self.bin_board

        for i in range(self.size):
            for j in range(self.size):
                neighbours = self.check_status(i + 1, j + 1)
                if neighbours == 2:
                    continue
                if neighbours == 3:
                    new_bin_board[i + 1][j + 1] = 1
                else:
                    new_bin_board[i + 1][j + 1] = 0

        self.bin_board = new_bin_board
        for i in range(self.size):
            for j in range(self.size):
                if self.bin_board[i + 1][j + 1] == 1:
                    self.board[i][j]['text'] = self.char
                else:
                    self.board[i][j]['text'] = ""
        Label(self.root, text="step: {}".format(self.step_count)).grid(columnspan=2, column=3,
                                                                       row=0, stick=W)
        self.root.after(time_step, lambda: self.step(time_step))

    def draw(self):
        self.clear()
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j]['state'] = DISABLED
                if random.randint(0, 2) == 1:
                    self.click(i, j)

    def clear(self):
        self.bin_board = [[0 for i in range(self.size + 2)] for j in range(self.size + 2)]
        for buttons in self.board:
            for button in buttons:
                button['text'] = ""
