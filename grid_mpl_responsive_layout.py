"""
Responsive/resizing GUI with a grid layout and Matplotlib charts.
No MPL charts yet though
"""
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from tkcalendar import DateEntry

class TabMySets(ttk.Frame):
    """
    This frame is where the user views their exercise sets.
    The user selects an exercise, and their sets are displayed in text and
    graphical view.
    """
    def __init__(self, parent):
        super().__init__(parent)

        # Most of our widgets are gridded directly onto this frame.
        # Here, we configure padding for this frame, which determines the spacing
        # between all widgets that are direct children of this frame.
        self.configure(padding=(3,3,12,12))

        # --- Define widgets ---
        # There are two frames placed on the root.
        # The Controls Frame will not resize as the window resizes?
        # The Display Frame will resize.
        #
        # self
        # |__frm_controls
        # |  |__ exercise + data selectors
        # |__frm_display
        #    |__ exercise sets + plot display
        self.frm_controls = ttk.Frame(self, padding=(3,3,12,12))
        self.lbl_exercise = ttk.Label(self.frm_controls, text="Exercise")
        self.combobox = ttk.Combobox(self.frm_controls, width=20)
        self.lbl_start_date = ttk.Label(self.frm_controls, text="Start Date")
        self.date_entry_start = DateEntry(self.frm_controls,
                                          width=12,
                                          background='darkblue',
                                          foreground='white',
                                          borderwidth=2)
        # self.date_entry_start.bind("<<DateEntrySelected>>", self.show_plots)
        self.lbl_end_date = ttk.Label(self.frm_controls, text="End Date")
        self.date_entry_end = DateEntry(self.frm_controls,
                                        width=12,
                                        background='darkblue',
                                        foreground='white',
                                        borderwidth=2)
        # self.date_entry_end.bind("<<DateEntrySelected>>", self.show_plots)


        self.frm_display = ttk.Frame(self, padding=(3,3,3,3))
        self.text_area = ScrolledText(self.frm_display, width=30)
        self.text_area.configure(state='disabled')  # user can't type here


        # --- Define data structures ---
        self.esd= {} # ESD = Exercises-Sets Dictionary. Maps 'exercise' -> [ExerciseSet]
        # self.update_exercises()

        # --- Manage layout of widgets ---
        self.frm_controls.grid(row=0, column=0, sticky='NSEW')
        self.lbl_exercise.grid(row=0, column=0)
        self.combobox.grid(row=0, column=1)
        self.lbl_start_date.grid(row=0, column=2)
        self.date_entry_start.grid(row=0, column=3)
        self.lbl_end_date.grid(row=0, column=4)
        self.date_entry_end.grid(row=0, column=5)

        self.frm_display.grid(row=1, column=0, sticky='NSEW')
        self.text_area.grid(row=0, column=0, sticky='NSW')

        # Configure the responsive layout for each row and column.
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.frm_display.rowconfigure(0, weight=1)
        self.frm_display.columnconfigure(0, weight=1)


root = Tk()

# DON'T FORGET TO SPECIFY STICKY AND ROWCONFIGURE/COLUMNCONFIGURE THE ROOT!
# The root is a widget like everything else.
tab = TabMySets(root)
tab.grid(row=0, column=0, sticky='NSEW')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
