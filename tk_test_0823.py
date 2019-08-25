#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *



class tree_view(ttk.Frame):
    """
    treeview設定
    """
    def __init__(self, master=None):
        super().__init__(master=master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.tree = ttk.Treeview(self)
        self.tree.pack()

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
        self.role_button = ttk.Button(button_frame, text="Create Role", width=10)
        self.key_button = ttk.Button(button_frame, text="Create API Key", width=10)
        self.role_button.pack()
        self.key_button.pack()

class overview(ttk.Frame):
    """
    全体windowの組み立て
    """

    def __init__(self, master=None):
        super().__init__(master=master)
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.create_role_frame()
        self.create_key_frame()
        self.create_button_frame()

    def create_role_frame(self):
        role_frame = ttk.Frame(self)
        role_frame.pack(side="left")
        role_frame_label = ttk.LabelFrame(role_frame, text="User Role")
        role_frame_label.pack(side="left")
        self.tree = tree_view(role_frame_label)

    def create_key_frame(self):
        key_frame = ttk.Frame(self)
        key_frame.pack(side="left")
        key_frame_label = ttk.LabelFrame(key_frame, text="API Key")
        key_frame_label.pack(side="left")
        self.tree = tree_view(key_frame_label)

    def create_button_frame(self):
        button_frame = ttk.Frame(self)
        button_frame.pack(side="left")
        self.button = button_view(button_frame) 


def main():
    root = tkinter.Tk()
    root.title("DS tool")
    root.geometry("600x500")
    overview(master=root)

    root.mainloop()

if __name__ == "__main__":
    main()
