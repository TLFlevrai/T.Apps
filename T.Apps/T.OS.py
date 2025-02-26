# T.OS.py
import tkinter as tk
from files.Apps import create_bottom_bar

root = tk.Tk()

root.title("Fenêtre Tkinter avec barre en bas")
root.geometry("600x400")

create_bottom_bar(root)

root.mainloop()