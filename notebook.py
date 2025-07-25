import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('1200x1000')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=1200, height=980)
frame2 = ttk.Frame(notebook, width=1200, height=980)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')


root.mainloop()