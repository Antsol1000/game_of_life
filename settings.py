import tkinter as tk
from tkinter import messagebox

TIME_STEP = 500

MAX_SIZE = 22
MIN_SIZE = 10


def start(board):
    """
    this function is used to call out Settings window
    """
    Settings(board)


class SettingException(Exception):
    """
    this is an exception class that pop up messagebox when show() is called
    """

    def show(self):
        messagebox.showerror("Error", self.__str__())


class CharException(SettingException):
    """
    CharException class inherits from SettingException
    it changes text in messagebox
    """

    def __str__(self):
        return "Char symbolizes living cell, it must be single character."


class SizeException(SettingException):
    """
    SizeException class inherits from SettingException
    it changes text in messagebox
    """

    def __str__(self):
        return "Size of the board must belong to <{}, {}>.".format(MIN_SIZE, MAX_SIZE)


class TimeStepException(SettingException):
    """
    TimeStepException class inherits from SettingException
    it changes text in messagebox
    """

    def __str__(self):
        return "Time step is length of day in milliseconds, it must be an integer."


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
        self.board = board
        # creates new window
        self.top = tk.Toplevel()
        self.top.title("SETTINGS")

        # creates entries for params
        self.char_entry = tk.Entry(self.top, width=10)
        self.char_entry.insert(0, self.board.char)
        self.size_entry = tk.Entry(self.top, width=10)
        self.size_entry.insert(0, self.board.size)
        self.time_step_entry = tk.Entry(self.top, width=10)
        self.time_step_entry.insert(0, TIME_STEP)

        # creates save_settings button
        self.save_button = tk.Button(self.top, text="SAVE SETTINGS",
                                     command=self.save_settings)

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

    def set_char(self):
        """
        sets param char, taken from entry
        """
        char = self.char_entry.get()
        if len(char) > 1:
            raise CharException
        else:
            self.board.char = char

    def set_size(self):
        """
        sets param size, taken from entry
        """
        size = int(self.size_entry.get())
        if size > MAX_SIZE or size < MIN_SIZE:
            raise SizeException
        else:
            self.board.size = size

    def set_time_step(self):
        """
        sets param TIME_STEP, taken from entry
        """
        global TIME_STEP
        try:
            TIME_STEP = int(self.time_step_entry.get())
        except Exception:
            raise TimeStepException

    def save_settings(self):
        """
        this function is called when one clicks save_button
        it sets all params, edits the board and destroy Settings window
        """
        # set param
        try:
            self.set_char()
            self.set_size()
            self.set_time_step()
        except SettingException as err:
            err.show()
        else:
            # edit the board and show new
            self.board.board = [[tk.Button(self.board.root, width=2, height=1,
                                           command=lambda r=j, c=i: self.board.click(r, c))
                                 for i in range(self.board.size)] for j in range(self.board.size)]
            self.board.bin_board = [[0 for i in range(self.board.size + 2)] for j in range(self.board.size + 2)]
            self.board.draw()
            self.board.show()
            self.board.show_buttons()

            # destroy Settings window
            self.top.destroy()
