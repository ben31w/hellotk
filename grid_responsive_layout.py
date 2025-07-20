"""
Stole this code:
https://tkdocs.com/tutorial/grid.html
"""
from tkinter import *
from tkinter import ttk

root = Tk()

# It's good convention to have a 'content' frame that all the widgets are placed
# on to, because you can adjust the padding of the 'content' frame.

# root
# |_content
#   |_frame
#   |_namelbl
#   |_etc.
content = ttk.Frame(root, padding=(3,3,12,12))
# width and height are starting points only
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

# sticky can enable a widget to stretch when the window is resized.
#  - by default, widgets in a grid layout will be centered inside their cell
#    and won't expand as the window grows. The parent widget fills in the empty
#    space.
#  - sticky enables the widget to stick to a certain edge or corner (ex: NW)
#  - it also enables the widget to stretch to fill empty space if two opposite
#    directions are specified (ex: NS)
#  - NOTE: sticky is not enough on its own to get widgets to stretch. You also
#    need to configure the rows and columns!!!!
content.grid(column=0, row=0, sticky=(N, S, E, W))
# NSEW = stick to center, and stretch in all directions
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
# NW = stick to top left, and don't stretch.
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
# NEW = stick to top, and stretch horizontally but not vertically
name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=5, padx=5)
# No sticky = no stretch
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

# rowconfigure and columnconfigure define how each row/col should be resized as
# the window resizes.
#  - If weight=1 for everything, then all rows/cols will resize equally.
#  - If weights are different, then some rows/cols will grow faster based on
#    weight ratio.
#  - NOTE: default weight for everything is 0 (don't expand)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()