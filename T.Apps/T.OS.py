# T.OS.py
import tkinter as tk
from files.Apps import create_bottom_bar

def change_background(color):
    if color == "black":
        root.config(bg="black")
        bottom_frame.config(bg="darkgray")
    else:
        root.config(bg="white")
        bottom_frame.config(bg="lightgray")

root = tk.Tk()

root.title("T.Apps")
root.geometry("600x400")

bottom_frame = create_bottom_bar(root, change_background)

root.mainloop()
