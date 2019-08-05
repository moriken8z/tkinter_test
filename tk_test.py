#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *


class test(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.label = tkinter.Label(self, text="ラベル テスト")
        self.entry = tkinter.Entry(self)
        self.button = tkinter.Button(self, text="ボタン テスト")
        self.check = tkinter.Checkbutton(self, text="チェック テスト")
        self.text = tkinter.Text(self)

        self.label.grid(column=0, row=0)
        self.entry.grid(column=1, row=0)
        self.button.grid(column=2, row=0)
        self.check.grid(column=0, row=1)
        self.text.grid(column=0, columnspan=3, row=2)




def main():
    root = tkinter.Tk()
    root.title("DS tool")
    root.geometry("500x500")
    test(master=root)

    root.mainloop()


if __name__ == "__main__":
    main()
