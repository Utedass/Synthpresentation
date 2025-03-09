import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initial parameters
freq = 1.0
amp = 1.0

# Function to update the plot
def update_plot():
    x = np.linspace(0, 4 * np.pi, 1000)
    y = amp * np.sin(freq * x)
    line.set_ydata(y)
    canvas.draw()

# Function to update parameters from sliders
def update_params(val):
    global freq, amp
    freq = float(freq_slider.get())
    amp = float(amp_slider.get())
    update_plot()

# Set up the Tkinter window
root = tk.Tk()
root.title("Sine Wave Interactive Plot")

# Matplotlib figure setup
fig, ax = plt.subplots()
x = np.linspace(0, 4 * np.pi, 1000)
y = amp * np.sin(freq * x)
line, = ax.plot(x, y, lw=2)
ax.set_ylim(-2, 2)
ax.set_xlim(0, 4 * np.pi)

# Embed Matplotlib figure in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Frequency slider
freq_slider = tk.Scale(root, from_=0.5, to=5.0, resolution=0.1, orient=tk.HORIZONTAL, label="Frequency", command=update_params)
freq_slider.set(freq)
freq_slider.pack()

# Amplitude slider
amp_slider = tk.Scale(root, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, label="Amplitude", command=update_params)
amp_slider.set(amp)
amp_slider.pack()

# Run Tkinter main loop
root.mainloop()
