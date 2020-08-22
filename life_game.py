from tkinter import *
import random


class Board:

    def __init__(self, root, size, char):
        self.char = char
        self.size = size
        self.board = [[Button(root, width=2, height=1,
                              command=lambda r=j, c=i: self.click(r, c))
                       for i in range(size)] for j in range(size)]
        self.bin_board = [[0 for i in range(size + 2)] for j in range(size + 2)]

    def click(self, row, column):
        self.board[row][column]['state'] = DISABLED
        self.board[row][column]['text'] = self.char

    def show(self):
        for i in range(self.size):
            for j in range(self.size):
                self.board[i][j].grid(row=i + 1, column=j)

    def start_game(self):
        for buttons in self.board:
            for button in buttons:
                button['state'] = DISABLED
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]['text'] == self.char:
                    self.bin_board[i + 1][j + 1] = 1

    def check_status(self, row, column):
        neighbours = self.bin_board[row - 1][column - 1] + self.bin_board[row - 1][column] + \
                     + self.bin_board[row - 1][column + 1] + self.bin_board[row][column - 1] + \
                     + self.bin_board[row][column + 1] + self.bin_board[row + 1][column - 1] + \
                     + self.bin_board[row + 1][column] + self.bin_board[row + 1][column + 1]
        return neighbours

    def step(self):
        new_board = self.board
        new_bin_board = self.bin_board
        for i in range(self.size):
            for j in range(self.size):
                neighbours = self.check_status(i + 1, j + 1)
                if neighbours == 2:
                    continue
                if neighbours == 3:
                    new_bin_board[i + 1][j + 1] = 1
                    new_board[i][j]['text'] = self.char
                else:
                    new_bin_board[i + 1][j + 1] = 0
                    new_board[i][j]['text'] = ""
        self.board = new_board
        self.bin_board = new_bin_board
        self.show()

    def draw(self):
        for buttons in self.board:
            for button in buttons:
                button['state'] = NORMAL
                if random.randint(0, 2) == 1:
                    button['text'] = self.char
                else:
                    button['text'] = ""
