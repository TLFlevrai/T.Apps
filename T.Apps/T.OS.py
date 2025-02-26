import tkinter as tk
from files.Apps import create_bottom_bar

def change_background(color):
    if color == "black":
        root.config(bg="black")
        bottom_frame.config(bg="darkgray")
    elif color == "blue":
        root.config(bg="#00A4D3")
        bottom_frame.config(bg="#007BB5")
    else:
        root.config(bg="white")
        bottom_frame.config(bg="lightgray")

root = tk.Tk()
root.title("Fenêtre Tkinter avec barre en bas")
root.geometry("600x400")

bottom_frame = create_bottom_bar(root, change_background)

root.mainloop()