import tkinter as tk
from files.Apps import create_bottom_bar
from programs.calculator import create_calculator

def change_background(color, text_label):
    if color == "black":
        root.config(bg="black")
        bottom_frame.config(bg="darkgray")
        text_label.config(bg="black", fg="white")
    elif color == "blue":
        root.config(bg="#00A4D3")
        bottom_frame.config(bg="#007BB5")
        text_label.config(bg="#00A4D3", fg="white")
    else:
        root.config(bg="white")
        bottom_frame.config(bg="lightgray")
        text_label.config(bg="white", fg="black")

root = tk.Tk()
root.title("Fenêtre Tkinter avec barre en bas")
root.geometry("600x400")

# Charger l'icône principale
root.iconbitmap("image/icon/calculator.ico")

bottom_frame = create_bottom_bar(root, change_background)

# Ajouter un bouton pour lancer l'application Calculator
calculator_button = tk.Button(root, text="Open Calculator", command=create_calculator)
calculator_button.pack(pady=10)

root.mainloop()
