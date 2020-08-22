from tkinter import *


class Settings:

    def __init__(self):
        self.top = Toplevel()
        self.top.title("SETTINGS")
        self.char = 'X'
        self.size = 20

        self.char_entry = Entry()
        self.size_entry = Entry()

    def set_char(self):
        pass

    def set_size(self):
        pass


def settings():
    sett = Settings()
