# files/Apps.py
import tkinter as tk

def create_bottom_bar(parent):
    bottom_frame = tk.Frame(parent, bg="lightgray", height=30)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    white_square = tk.Label(bottom_frame, bg="white", width=4, height=2, relief="solid", borderwidth=2)
    white_square.pack(pady=5, padx=10, side=tk.LEFT)

    black_square = tk.Label(bottom_frame, bg="black", width=4, height=2, relief="solid", borderwidth=2)
    black_square.pack(pady=5, padx=10, side=tk.LEFT)

    return bottom_frame