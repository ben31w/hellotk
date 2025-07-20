# It's tkinter convention to use the wildcard import.
# ttk is a submodule of tkinter that includes themed widgets.
from tkinter import *
from tkinter import ttk

# Tkinter GUIs are often classes like this.
class FeetToMeters:
    def __init__(self, root: Tk):
        root.title("Feet to Meters")

        # Create a Frame widget to hold the content, and place it in the main application window.
        # You could also place content directly on the main window instead of the frame,
        # but it's better practice to use a frame because its background color will match
        # other themed widgets.
        # rowconfigure/columnconfigure tell the frame to expand to fill extra space when
        # the window is resized.  ???
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=NSEW)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Create an Entry widget (for text entry)
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)  # specify parent in constructor
        feet_entry.grid(column=2, row=1, sticky=EW)  # place it inside the parent with grid()

        # Rest of widgets
        self.meters = StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=EW)

        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        # Shortcut for adding padding to each widget
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        # Initial focus is on the Entry widget when the app starts
        feet_entry.focus()
        # Bind Return/Enter key to calculate
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass


# Main application window
root = Tk()
FeetToMeters(root)
root.mainloop()