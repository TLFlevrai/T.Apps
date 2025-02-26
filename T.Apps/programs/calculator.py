import tkinter as tk
from tkinter import messagebox

def create_calculator():
    calc_window = tk.Toplevel()
    calc_window.title("Calculator")
    calc_window.geometry("400x400")

    # Charger l'icône
    calc_window.iconbitmap("image/icon/calculator.ico")

    # Exemple d'un bouton de calcul
    label = tk.Label(calc_window, text="Enter a calculation:")
    label.pack(pady=10)

    entry = tk.Entry(calc_window)
    entry.pack(pady=10)

    def calculate():
        try:
            result = eval(entry.get())  # Utilisation de eval pour le calcul
            messagebox.showinfo("Result", f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    calc_button = tk.Button(calc_window, text="Calculate", command=calculate)
    calc_button.pack(pady=10)

    calc_window.mainloop()

