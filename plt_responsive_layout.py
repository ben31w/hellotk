"""
Tkinter GUI with MatPlotLib PyPlot figures that scale responsively based
on screen size.
"""
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from screeninfo import get_monitors

# --- Get screen size ---
for m in get_monitors():
    print(f"Monitor: {m.name}, {m.width}x{m.height}, at ({m.x}, {m.y}){', PRIMARY' if m.is_primary else ''}")
    if m.is_primary:
        screen_width = m.width
        screen_height = m.height

try:
    # Scale relative to 1080p. If screen width < 1920 or screen height < 1080,
    # shrink everything so it displays nicely.
    scale = min(screen_width / 1920, screen_height / 1080)
    print(f"Scale: {scale}")
except NameError:
    print("Failed to find a primary monitor.")
    exit(1)

# --- Tkinter setup ---
root = tk.Tk()
root.title("Dynamic Matplotlib Scaling")

root.geometry("800x600")
root.update()

# --- Base dimensions ---
base_figsize = (8, 5)
base_title_size = 20
base_label_size = 14
base_tick_size = 12
base_legend_size = 12

# --- Scale everything ---
figsize = (base_figsize[0] * scale, base_figsize[1] * scale)
title_size = base_title_size * scale
label_size = base_label_size * scale
tick_size = base_tick_size * scale
legend_size = base_legend_size * scale

# --- Create figure ---
fig, ax = plt.subplots(figsize=figsize)
ax.plot([1, 2, 3], [1, 4, 9], label="Data")
ax.set_title("Dynamic Plot", fontsize=title_size)
ax.set_xlabel("X Axis", fontsize=label_size)
ax.set_ylabel("Y Axis", fontsize=label_size)
ax.tick_params(labelsize=tick_size)
ax.legend(fontsize=legend_size)

# --- Embed in Tkinter ---
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()

