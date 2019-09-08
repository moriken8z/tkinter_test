#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *


class get_info():
    """
    APIによる情報取得
    """
    #def __init__(self, master=None):
    #    super().__init__(master=master)

    def get_users_info(self):
        self.users = {
            "MasterAdmin":["ja-Jp", "UTC+9", "xxx"],
            "test_User1":["en-US", "UTC+0", "xxx"],
            "test_User2":["ja-JP", "UTC+9", "xxx"],
            }
        return self.users
    
    def get_roles_info(self):
        self.roles = {
            "Full Access":["all computers", "policy", "hoge"],
            "Auditor":["xxx", "xxx", "xxx"],
            "test Role":["xxx", "xxx", "xxx"],
            }
        return self.roles

    def get_api_keys_info(self):
        self.api_keys = {
            "API Key1":["test1", "en-US", "1"],
            "API Key2":["test2", "ja-JP", "2"],
            "API Key3":["test3", "ja-JP", "3"],
            }
        return self.api_keys

class users_tree_view(ttk.Frame):
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

        Users = get_info().get_users_info()

        for x in Users:
            root_node = self.tree.insert(
                "",     #最上位なのでparentは空文字
                "end",
                text=x,
                )
            #辞書の要素を挿入
            for y in Users[x]:
                self.tree.insert(
                    root_node,  #parentはキーの認識番号
                    "end",
                    text=y,
                    )

class roles_tree_view(ttk.Frame):
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

        Roles = get_info().get_roles_info()

        for x in Roles:
            root_node = self.tree.insert(
                "",     #最上位なのでparentは空文字
                "end",
                text=x,
                )
            #辞書の要素を挿入
            for y in Roles[x]:
                self.tree.insert(
                    root_node,  #parentはキーの認識番号
                    "end",
                    text=y,
                    )       

class keys_tree_view(ttk.Frame):
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

        API_keys = get_info().get_api_keys_info()

        for x in API_keys:
            root_node = self.tree.insert(
                "",     #最上位なのでparentは空文字
                "end",
                text=x,
                )
            #辞書の要素を挿入
            for y in API_keys[x]:
                self.tree.insert(
                    root_node,  #parentはキーの認識番号
                    "end",
                    text=y,
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
        self.tree = users_tree_view(user_frame_label)

    def create_role_frame(self):
        role_frame = ttk.Frame(self)
        role_frame.pack(side="left")
        role_frame_label = ttk.LabelFrame(role_frame, text="Roles", width=200)
        role_frame_label.pack(side="left")
        self.tree = roles_tree_view(role_frame_label)

    def create_key_frame(self):
        key_frame = ttk.Frame(self)
        key_frame.pack(side="left")
        key_frame_label = ttk.LabelFrame(key_frame, text="API Keys")
        key_frame_label.pack(side="left")
        self.tree = keys_tree_view(key_frame_label)

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
