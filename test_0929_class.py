#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk

class main_frame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title('DS Tool')
        master.geometry('950x300')

        f0 = ttk.LabelFrame(master, width=250, height=200, text='Users')
        f1 = ttk.LabelFrame(master, width=250, height=200, text='Roles')
        f2 = ttk.LabelFrame(master, width=250, height=200, text='API keys')
        f3 = ttk.LabelFrame(master, width=100, height=200, text='Settings')

        f0.grid(padx = 5, pady = 5, ipadx = 5, ipady = 5)
        f0.columnconfigure(0, weight=1)
        f0.rowconfigure(0, weight=1)
        f0.grid_propagate(False)

        f1.grid(row=0, column=1, padx = 5, pady = 5, ipadx = 5, ipady = 5)
        f1.columnconfigure(0, weight=1)
        f1.rowconfigure(0, weight=1)
        f1.grid_propagate(False)
        
        f2.grid(row=0, column=2, padx = 5, pady = 5, ipadx = 5, ipady = 5)
        f2.columnconfigure(0, weight=1)
        f2.rowconfigure(0, weight=1)
        f2.grid_propagate(False)

        f3.grid(row=0, column=3, padx = 5, pady = 5, ipadx = 5, ipady = 5)
        f3.columnconfigure(0, weight=1)
        f3.grid_propagate(False)


if __name__ == '__main__':
    root = tkinter.Tk()
    app = main_frame(master=root)
    app.mainloop()