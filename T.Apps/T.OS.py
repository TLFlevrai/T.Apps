import tkinter as tk

root = tk.Tk()

root.title("Fenêtre Tkinter avec barre en bas")
root.geometry("600x400")

bottom_frame = tk.Frame(root, bg="lightgray", height=30)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

square = tk.Label(bottom_frame, bg="white", width=4, height=2, relief="solid", borderwidth=2)
square.pack(pady=5, padx=10, side=tk.LEFT)

root.mainloop()
