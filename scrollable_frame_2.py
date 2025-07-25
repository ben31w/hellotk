"""
https://www.tutorialspoint.com/implementing-a-scrollbar-using-grid-manager-on-a-tkinter-window

with some mousewheel logic from ChatGPT
"""
import platform
import tkinter as tk
from tkinter import ttk


def bind_mousewheel():
   system = platform.system()
   if system == "Windows" or system == "Darwin":  # Darwin = macOS
      canvas.bind_all("<MouseWheel>", on_mousewheel)
   else:  # Assume Linux
      canvas.bind_all("<Button-4>", on_mousewheel_linux)
      canvas.bind_all("<Button-5>", on_mousewheel_linux)

def on_mousewheel(event):
   # For Windows/macOS
   canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def on_mousewheel_linux(event):
   # For Linux (event.num = 4 = up, 5 = down)
   if event.num == 4:
      canvas.yview_scroll(-1, "units")
   elif event.num == 5:
      canvas.yview_scroll(1, "units")

# Step 2: Create the Tkinter Window
root = tk.Tk()
root.title("Scrollable Grid Example")
root.geometry("720x250")

# Step 3: Create a Frame for Grid Layout
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

# Step 4: Create a Canvas and Scrollbar
canvas = tk.Canvas(frame)
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Step 5: Create a Frame for Scrollable Content
content_frame = ttk.Frame(canvas)

# Step 6: Configure the Canvas and Scrollable Content Frame
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Step 7: Add Widgets to the Content Frame
# Example widgets (replace with your own)
label = ttk.Label(content_frame, text="Scrollable Content")
label.grid(row=0, column=0, pady=10)

for i in range(1, 21):
   button = ttk.Button(content_frame, text=f"Button {i}")
   button.grid(row=i, column=0, pady=5)

# Step 8: Create Window Resizing Configuration
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Step 9: Pack Widgets onto the Window
canvas.create_window((0, 0), window=content_frame, anchor="nw")
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Step 10: Bind the Canvas to Mousewheel Events
bind_mousewheel()

# Step 11: Run the Tkinter Event Loop
root.mainloop()