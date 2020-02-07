from tkinter import *
import tkinter as tk
from functools import partial


if __name__ == '__main__':
    root = Tk()
    root.minsize(200,200)
    user_label = tk.Label(root,text = "enter user name")
    user_entry = tk.Entry(root)
    stalk_buton = tk.Button(root,text = "stalk")
    user_label.place(x = 20, y = 30 + 1*30, width=120, height=25)
    user_entry.place(x = 20, y = 30 + 2*30, width=120, height=25)
    stalk_buton.place(x = 20, y = 30 + 3*30, width=120, height=25)
    user_label.Border = tk.Frame(relief='flat', borderwidth=10)
    user_entry.Border = tk.Frame(relief='flat', borderwidth=10)
    stalk_buton.Border = tk.Frame(relief='flat', borderwidth=10)
    root.mainloop()

