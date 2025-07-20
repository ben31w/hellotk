"""
Press a button to dynamically populate the window with plots.
"""
from tkinter import *
from tkinter import ttk

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
from matplotlib.colors import Colormap
from matplotlib.figure import Figure


def show_plots():
    show_plot("1", 0, 1)
    show_plot("2", 0, 2)

def show_plot(title, row, column):
    fig = Figure(figsize=(1,1))
    ax = fig.add_subplot(111)
    fig.suptitle(title)

    x = [1, 2, 3]
    y = [1, 2, 3]

    ax.plot(x, y)

    canvas = FigureCanvasTkAgg(fig, row1)
    canvas.draw()
    canvas.get_tk_widget().grid(row=row, column=column)
    print(canvas.get_width_height())

root = Tk()
frm = ttk.Frame(root)
frm.pack()
row1 = ttk.Frame(frm)

# Row 0
btn = ttk.Button(frm, text='Press', command=show_plots)
btn.grid(row=0, column=0, sticky=W)

# Row 1
row1.grid(row=1, column=0)
text_area = Text(row1, height=40, width=30)
text_area.grid(row=0, column=0)
frm_grid = ttk.Frame(row1)
frm_grid.grid(row=0, column=1)


frm_plot_tl = ttk.Frame(frm_grid, width=80, height=80)
frm_plot_tl.grid(row=0, column=0)
frm_plot_tr = ttk.Frame(frm_grid, width=80, height=80)
frm_plot_tr.grid(row=0, column=1)
frm_plot_bl = ttk.Frame(frm_grid, width=80, height=80)
frm_plot_bl.grid(row=1, column=0)
frm_plot_br = ttk.Frame(frm_grid, width=80, height=80)
frm_plot_br.grid(row=1, column=1)

frm_grid.grid_propagate(False)

root.mainloop()

