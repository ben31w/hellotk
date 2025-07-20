"""
Example using place layout manager.
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x480")

mainframe = Frame(root, background="bisque")
labelframe = Frame(mainframe, background="pink")
buttonframe = Frame(mainframe, background="yellow")

mainframe.place(x=0, y=0, anchor="nw", width=385, height=460)
labelframe.place(x=0, y=0, anchor="nw", width=375, height=115)
buttonframe.place(x=0, y=116, anchor="nw", width=375, height=330)

root.mainloop()