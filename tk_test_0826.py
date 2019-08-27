#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *


class user_view(ttk.Frame):
    """
    Usersのtreeview設定
    """
    def __init__(self, master=None):
        super().__init__(master=master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.tree = ttk.Treeview(self)
        self.tree.pack()
    
        menu = {
            "Food":["Hamburger", "Beef steak", "Salad"],
            "Softdrink":["Coke", "Cider", "Tea"],
            "Alcohol":["Beer", "Wine", "Cocktail"],
            }

        for p in menu:
            root_node = self.tree.insert(
                "",     #最上位なのでparentは空文字
                "end",
                text=p,
                )
            #辞書の要素を挿入
            for m in menu[p]:
                self.tree.insert(
                    root_node,  #parentはキーの認識番号
                    "end",
                    text=m,
                    )

class role_view(ttk.Frame):
    """
    Rolesのtreeview設定
    """
    def __init__(self, master=None):
        super().__init__(master=master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.tree = ttk.Treeview(self)
        self.tree.pack()

        menu = {
            "Food":["Hamburger", "Beef steak", "Salad"],
            "Softdrink":["Coke", "Cider", "Tea"],
            "Alcohol":["Beer", "Wine", "Cocktail"],
            }

        for p in menu:
            root_node = self.tree.insert(
                "",     #最上位なのでparentは空文字
                "end",
                text=p,
                )
            #辞書の要素を挿入
            for m in menu[p]:
                self.tree.insert(
                    root_node,  #parentはキーの認識番号
                    "end",
                    text=m,
                    )       

class key_view(ttk.Frame):
    """
    Api Keysのtreeview設定
    """
    def __init__(self, master=None):
        super().__init__(master=master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.tree = ttk.Treeview(self)
        self.tree.pack()

        menu = {
            "Food":["Hamburger", "Beef steak", "Salad"],
            "Softdrink":["Coke", "Cider", "Tea"],
            "Alcohol":["Beer", "Wine", "Cocktail"],
            }

        for p in menu:
            root_node = self.tree.insert(
                "",     #最上位なのでparentは空文字
                "end",
                text=p,
                )
            #辞書の要素を挿入
            for m in menu[p]:
                self.tree.insert(
                    root_node,  #parentはキーの認識番号
                    "end",
                    text=m,
                    )

class button_view(ttk.Frame):
    """
    button設定
    """
    def __init__(self, master=None):
        super().__init__(master=master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.create_add_button()

    def create_add_button(self):
        button_frame = ttk.Frame(self)
        button_frame.pack()
        self.get_info_button = ttk.Button (
                                            button_frame,
                                            text="Get Info",
                                            )
        self.user_button = ttk.Button(
                                        button_frame,
                                        text="Create User",
                                        command=self.user_sub_window
                                        )
        self.role_button = ttk.Button(
                                        button_frame,
                                        text="Create Role",
                                        command=self.role_sub_window
                                        )
        self.key_button = ttk.Button(
                                        button_frame,
                                        text="Create API key",
                                        command=self.key_sub_window
                                        )
        self.get_info_button.pack(fill="x")
        self.user_button.pack(fill="x")
        self.role_button.pack(fill="x")
        self.key_button.pack(fill="x")

    def user_sub_window(self):
        #サブウィンドウ作成
        self.sub_win = Toplevel()

        #サブウィンドウの画面サイズ
        self.sub_win.geometry("300x200")

        self.sub_win_frame = ttk.Frame(self.sub_win)
        self.sub_win_frame.pack()
        self.sub_win_label = ttk.Label(self.sub_win_frame, text="name")
        self.sub_win_label.pack()


        self.sub_win_entry = ttk.Entry(self.sub_win, width=20)
        self.sub_win_entry.pack()

        #サブウィンドウのボタン生成
        self.sub_win_button = ttk.Button(
                                            self.sub_win,
                                            text="Create",
                                            width=str("Create"),
                                            command=self.sub_win.destroy
                                        )
        self.sub_win_button.pack()
        



    def role_sub_window(self):
        #サブウィンドウ作成
        self.sub_win = Toplevel()

        #サブウィンドウの画面サイズ
        self.sub_win.geometry("300x200")

        #サブウィンドウのボタン生成
        self.sub_win_button = ttk.Button(
                                            self.sub_win,
                                            text="Create",
                                            width=str("Create"),
                                            command=self.sub_win.destroy
                                        )
        self.sub_win_button.pack()

    def key_sub_window(self):
        #サブウィンドウ作成
        self.sub_win = Toplevel()

        #サブウィンドウの画面サイズ
        self.sub_win.geometry("300x200")

        #サブウィンドウのボタン生成
        self.sub_win_button = ttk.Button(
                                            self.sub_win,
                                            text="Create",
                                            width=str("Create"),
                                            command=self.sub_win.destroy
                                        )
        self.sub_win_button.pack()

class overview(ttk.Frame):
    """
    全体windowの組み立て
    """

    def __init__(self, master=None):
        super().__init__(master=master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.create_user_frame()
        self.create_role_frame()
        self.create_key_frame()
        self.create_button_frame()

    def create_user_frame(self):
        user_frame = ttk.Frame(self)
        user_frame.pack(side="left")
        user_frame_label = ttk.LabelFrame(user_frame, text="Users")
        user_frame_label.pack(side="left")
        self.tree = user_view(user_frame_label)

    def create_role_frame(self):
        role_frame = ttk.Frame(self)
        role_frame.pack(side="left")
        role_frame_label = ttk.LabelFrame(role_frame, text="Roles", width=200)
        role_frame_label.pack(side="left")
        self.tree = role_view(role_frame_label)

    def create_key_frame(self):
        key_frame = ttk.Frame(self)
        key_frame.pack(side="left")
        key_frame_label = ttk.LabelFrame(key_frame, text="API Keys")
        key_frame_label.pack(side="left")
        self.tree = key_view(key_frame_label)

    def create_button_frame(self):
        button_frame = ttk.Frame(self, width=20)
        button_frame.pack(side="left")
        self.button = button_view(button_frame) 


def main():
    root = tkinter.Tk()
    root.title("DS tool")
    root.geometry("1000x500")
    overview(master=root)

    root.mainloop()

if __name__ == "__main__":
    main()
