import tkinter as tk

def create_bottom_bar(parent, change_background):
    bottom_frame = tk.Frame(parent, bg="lightgray", height=30)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    white_square = tk.Label(bottom_frame, bg="white", width=4, height=2, relief="solid", borderwidth=2)
    white_square.pack(pady=5, padx=10, side=tk.LEFT)

    black_square = tk.Label(bottom_frame, bg="black", width=4, height=2, relief="solid", borderwidth=2)
    black_square.pack(pady=5, padx=10, side=tk.LEFT)

    windows7_blue = "#00A4D3"
    blue_square = tk.Label(bottom_frame, bg=windows7_blue, width=4, height=2, relief="solid", borderwidth=2)
    blue_square.pack(pady=5, padx=10, side=tk.LEFT)

    white_square.bind("<Button-1>", lambda event: change_background("white"))
    black_square.bind("<Button-1>", lambda event: change_background("black"))
    blue_square.bind("<Button-1>", lambda event: change_background("blue"))

    return bottom_frame