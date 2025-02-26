import tkinter as tk

root = tk.Tk()

root.title("Fenêtre Tkinter avec barre en bas")
root.geometry("400x300")

bottom_frame = tk.Frame(root, bg="lightgray", height=30)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()