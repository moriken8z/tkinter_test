#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *


menu = {
        "Food":["Hamburger", "Beef steak", "Salad"],
        "Softdrink":["Coke", "Cider", "Tea"],
        "Alcohol":["Beer", "Wine", "Cocktail"],
        }

menu2 = {
        "test":["Hamburger", "Beef steak", "Salad"],
        "test1":["Coke", "Cider", "Tea"],
        "test2":["Beer", "Wine", "Cocktail"],
        }


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
        self.tree1 = ttk.Treeview(self)
        self.tree2 = ttk.Treeview(self)

        self.label.grid(column=0, row=0)
        self.entry.grid(column=1, row=0)
        self.button.grid(column=2, row=0)
        self.check.grid(column=0, row=1)
        self.tree1.grid(column=0, columnspan=3, row=2)
        self.tree2.grid(column=0, columnspan=4, row=3)

        for p in menu:
            root_node = self.tree1.insert(
                "",     #最上位なのでparentは空文字
                "end",
                text=p,
                )
            #辞書の要素を挿入
            for m in menu[p]:
                self.tree1.insert(
                    root_node,  #parentはキーの認識番号
                    "end",
                    text=m,
                    )
 
        for p in menu2:
            root_node = self.tree2.insert(
                "",     #最上位なのでparentは空文字
                "end",
                text=p,
                )
            #辞書の要素を挿入
            for m in menu2[p]:
                self.tree2.insert(
                    root_node,  #parentはキーの認識番号
                    "end",
                    text=m,
                    )


def main():
    root = tkinter.Tk()
    root.title("DS tool")
    root.geometry("500x500")
    test(master=root)

    root.mainloop()


if __name__ == "__main__":
    main()
