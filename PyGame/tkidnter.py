import tkinter as tk

root = tk.Tk()
# Create a button with a 'star' cursor
button = tk.Button(root, text="Click Me", cursor="star")
button.pack()

root.mainloop()