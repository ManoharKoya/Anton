from tkinter import *
import tkinter as tk
from functools import partial

# def get_recent_request():
#     return "the life after death is not so interesting."

def get_recent_comment():
    return "the life after death is not so interesting."
def get_analysis_text():
    return "the life after death is not so interesting."
def print_graph():
        pass
def get_recent_requests():
    request_window = Tk()
    label_text = get_recent_request()
    label = tk.Label(request_window,text = label_text)
    label.pack()
    request_window.mainloop()

def close(root):
    root.destroy()

def recent_comments():
    comment_window = Tk()
    label_text = get_recent_comment()
    label = tk.Label(comment_window,text = label_text)
    label.pack()
    comment_window.mainloop()
def show_analysis():
    analysis_window= Tk()
    analysis_text = get_analysis_text()
    analysis_label = tk.Label(analysis_window,tetxt = analysis_label,command = print_graph())
    analysis_label.pack()


if __name__ == '__main__':
    root = Tk()
    root.minsize(150,150)
    getreplies = Button(root,text = 'replies',command = get_recent_requests)
    close = Button(root,text = 'close', command = partial(close,root))
    getcomments = Button(root,text= 'get comments' , command = recent_comments)
    analysis_button = Button(root, text = 'show analysis' , command = show_analysis)
    getreplies.pack()
    getcomments.pack()
    analysis_button.pack()
    close.pack()
    root.mainloop()