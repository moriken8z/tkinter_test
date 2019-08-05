#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk

#1. 辞書表示用ツリービュークラス
class TestTreeview(ttk.Treeview):
    def __init__(self, master=None):
        super().__init__(master=master)
        menu = {
            "Food":["Hamburger", "Beef steak", "Salad"],
            "Softdrink":["Coke", "Cider", "Tea"],
            "Alcohol":["Beer", "Wine", "Cocktail"],
            }

        #辞書のキーを挿入
        for p in menu:
            root_node = self.insert(
                "",     #最上位なのでparentは空文字
                "end",
                text=p,
                )
            #辞書の要素を挿入
            for m in menu[p]:
                self.insert(
                    root_node,  #parentはキーの認識番号
                    "end",
                    text=m,
                    )

if __name__ == "__main__":
    root = tkinter.Tk()
    #2.ツリービューの表示
    t = TestTreeview(master=root)
    t.pack()

    root.mainloop()
