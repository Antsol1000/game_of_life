from tkinter import *


class Settings:

    def __init__(self):
        self.char = "X"
        self.size = 20

        # creates new window
        self.top = Toplevel()
        self.top.title("SETTINGS")

        # creates entries for params
        self.char_entry = Entry(self.top)
        self.char_entry.insert(0, 'X')
        self.size_entry = Entry(self.top)
        self.size_entry.insert(0, '20')

        # creates save_settings button
        self.save_button = Button(self.top, text="SAVE SETTINGS", command=self.save_settings)

        self.show()

    def show(self):
        Label(self.top, text="CHAR: ").grid(row=0, column=0)
        self.char_entry.grid(row=0, column=1)
        Label(self.top, text="SIZE: ").grid(row=1, column=0)
        self.size_entry.grid(row=1, column=1)

        self.save_button.grid(row=2, columnspan=2)

    def set_char(self):
        self.char = self.char_entry.get()

    def set_size(self):
        self.size = int(self.size_entry.get())

    def save_settings(self):
        self.set_char()
        self.set_size()
        self.top.destroy()
