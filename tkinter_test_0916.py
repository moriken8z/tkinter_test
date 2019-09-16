#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
from tkinter import ttk

menu = {
    "Fooooooooooooooooooooooooooooooooooood":["Hamburger", "Beef steak", "Salad"],
    "Softdrink":["Cokeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "Cider", "Tea"],
    "Alcohol":["Beer", "Wine", "Cocktail"],
    }


root = tkinter.Tk()
root.title('DS Tool')
root.geometry('850x300')

f0 = ttk.LabelFrame(root, width=200, height=200, text='Users')
f1 = ttk.LabelFrame(root, width=200, height=200, text='Roles')
f2 = ttk.LabelFrame(root, width=200, height=200, text='API keys')
f3 = ttk.LabelFrame(root, width=200, height=200, text='Settings')

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


tree0 = ttk.Treeview(f0)
tree0["columns"]=(1,2,3)
tree0.heading("#0", text="")
tree0.heading(1, text="item")
tree0.heading(2, text="value")

tree0.column("#0", minwidth=50, stretch=False, width=50)
tree0.column(1, minwidth=50, stretch=False, width=50)
tree0.column(2, minwidth=50, stretch=False, width=50)

xScrollbar = ttk.Scrollbar(f0, orient='horizontal')
xScrollbar.config(command=tree0.xview)
yScrollbar = ttk.Scrollbar(f0, orient='vertical', command=tree0.yview)
yScrollbar.config(command=tree0.yview)
tree0.config(xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set)

tree0.grid(row=0, column=0, sticky='NEWS')
xScrollbar.grid(row=1, column=0, sticky='EW')
yScrollbar.grid(row=0, column=1, sticky='NS')

for p in menu:
    root_node = tree0.insert(
        "",     #最上位なのでparentは空文字
        "end",
        text=p,
        )
    #辞書の要素を挿入
    for m in menu[p]:
        tree0.insert(
            root_node,  #parentはキーの認識番号
            "end",
            text=m,
            )


tree1 = ttk.Treeview(f1)
tree1["columns"]=(1,2,3)
tree1.heading("#0", text="")
tree1.heading(1, text="item")
tree1.heading(2, text="value")

tree1.column("#0", minwidth=50, stretch=False, width=50)
tree1.column(1, minwidth=50, stretch=False, width=50)
tree1.column(2, minwidth=50, stretch=False, width=50)

xScrollbar1 = ttk.Scrollbar(f1, orient='horizontal')
xScrollbar1.config(command=tree0.xview)

yScrollbar1 = ttk.Scrollbar(f1, orient='vertical', command=tree1.yview)
yScrollbar1.config(command=tree1.yview)

tree1.config(xscrollcommand=xScrollbar1.set, yscrollcommand=yScrollbar1.set)

tree1.grid(row=0, column=0, sticky='NEWS')
xScrollbar1.grid(row=1, column=0, sticky='EW')
yScrollbar1.grid(row=0, column=1, sticky='NS')

for p in menu:
    root_node = tree1.insert(
        "",     #最上位なのでparentは空文字
        "end",
        text=p,
        )
    #辞書の要素を挿入
    for m in menu[p]:
        tree1.insert(
            root_node,  #parentはキーの認識番号
            "end",
            text=m,
            )


tree2 = ttk.Treeview(f2)
tree2["columns"]=(1,2,3)
tree2.heading("#0", text="")
tree2.heading(1, text="item")
tree2.heading(2, text="value")

tree2.column("#0", minwidth=50, stretch=False, width=50)
tree2.column(1, minwidth=50, stretch=False, width=50)
tree2.column(2, minwidth=50, stretch=False, width=50)

xScrollbar2 = ttk.Scrollbar(f2, orient='horizontal')
xScrollbar2.config(command=tree2.xview)

yScrollbar2 = ttk.Scrollbar(f2, orient='vertical', command=tree2.yview)
yScrollbar2.config(command=tree1.yview)

tree2.config(xscrollcommand=xScrollbar2.set, yscrollcommand=yScrollbar2.set)

tree2.grid(row=0, column=0, sticky='NEWS')
xScrollbar2.grid(row=1, column=0, sticky='EW')
yScrollbar2.grid(row=0, column=1, sticky='NS')

for p in menu:
    root_node = tree2.insert(
        "",     #最上位なのでparentは空文字
        "end",
        text=p,
        )
    #辞書の要素を挿入
    for m in menu[p]:
        tree2.insert(
            root_node,  #parentはキーの認識番号
            "end",
            text=m,
            )


button0 = ttk.Button(f3, text='Get Info')
button1 = ttk.Button(f3, text='Create Users')
button2 = ttk.Button(f3, text='Create Roles')
button3 = ttk.Button(f3, text='Create API keys')

button0.grid(row=1, column=0, sticky='EW')
button1.grid(row=2, column=0, sticky='EW')
button2.grid(row=3, column=0, sticky='EW')
button3.grid(row=4, column=0, sticky='EW')

#最後に
root.mainloop()

