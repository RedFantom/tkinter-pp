import tkinter as tk
from tkinterpp import CreateToolTip


window = tk.Tk()
button = tk.Button(window, text="Hello World", command=window.destroy)
CreateToolTip(button)
button.pack()
window.mainloop()
