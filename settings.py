import math
import tkinter as tk
import enum
from tkinter import messagebox

""" length of day in milliseconds"""
TIME_STEP = 500

""" MAX and MIN size of the board"""
MAX_SIZE = 22
MIN_SIZE = 10

""" relative path to program icon """
ICON_PATH = "bin\\ant_icon.ico"


class Color(enum.Enum):
    """
    Color contains hex representation of common colors
    Feel free to add new colors
    """
    RED = "#ff0000"
    GREEN = "#00ff00"
    BLUE = "#0000ff"
    BLACK = "#000000"
    TURQUOISE = "#40e0d0"
    HOT_PINK = "#ff69b4"
    YELLOW = "#ffff00"
    ORANGE = "#ffa500"
    BRITISH_RACING_GREEN = "#004225"


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


class SmallerSizeException(SettingException):
    """
    SmallerSizeException class inherits from SettingException
    it changes text in messagebox
    it is called when one want to shrink down the board
    """

    def __str__(self):
        return "If you want to shrink down the size you have to restart the program."


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
        creates new window, entries for params, color buttons and save button param
        at the end it calls self.show() which grids all the stuff
        """
        self.board = board
        # creates new window
        self.top = tk.Toplevel()
        self.top.title("SETTINGS")
        self.top.iconbitmap(ICON_PATH)

        # creates entries for params
        self.char_entry = tk.Entry(self.top, width=11)
        self.char_entry.insert(0, self.board.char)
        self.size_entry = tk.Entry(self.top, width=11)
        self.size_entry.insert(0, self.board.size)
        self.time_step_entry = tk.Entry(self.top, width=11)
        self.time_step_entry.insert(0, TIME_STEP)

        # creates color buttons
        self.color_buttons = [tk.Button(self.top, width=2, height=1, bg=color.value,
                                        command=lambda color=color: self.color_button_click(color)) for color in Color]

        # creates save_settings button
        self.save_button = tk.Button(self.top, text="SAVE SETTINGS",
                                     command=self.save_settings)

        self.show()

    def show(self):
        """
        grids entries and labels for params
        grids color_buttons
        grids save_button
        """
        tk.Label(self.top, text="CHAR: ").grid(row=0, column=0, stick=tk.W)
        self.char_entry.grid(row=0, column=1, columnspan=4)
        tk.Label(self.top, text="SIZE: ").grid(row=1, column=0, stick=tk.W)
        self.size_entry.grid(row=1, column=1, columnspan=4)
        tk.Label(self.top, text="TIME STEP [ms]: ").grid(row=2, column=0, stick=tk.W)
        self.time_step_entry.grid(row=2, column=1, columnspan=4)

        # show color buttons, make active color DISABLED, 3 colors in row
        tk.Label(self.top, text="COLOR: ").grid(row=3, column=0, stick=tk.W)
        i = 0
        for color_button in self.color_buttons:
            if color_button['bg'] == self.board.color:
                color_button['state'] = tk.DISABLED
                color_button['text'] = "X"
            color_button.grid(row=3 + i // 3, column=1 + i % 3)
            i += 1

        self.save_button.grid(row=3 + math.ceil(len(Color) / 3), columnspan=2 + len(Color))

    def color_button_click(self, color):
        """
        called when click color_button
        makes another button NORMAL
        put X in clicked button
        :param color: color of clicked button
        """
        for color_button in self.color_buttons:
            if color_button['bg'] == color.value:
                color_button['state'] = tk.DISABLED
                color_button['text'] = "X"
            else:
                color_button['state'] = tk.NORMAL
                color_button['text'] = ""

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
        elif size < self.board.size:
            raise SmallerSizeException
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

    def set_color(self):
        """
        sets color that is clicked
        """
        for color_button in self.color_buttons:
            if color_button['state'] == tk.DISABLED:
                self.board.color = color_button['bg']

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
            self.set_color()
        except SettingException as err:
            err.show()
        else:
            # edit the board and show new
            self.board.board_init()
            self.board.draw()
            self.board.show()
            self.board.show_buttons()

            # destroy Settings window
            self.top.destroy()
