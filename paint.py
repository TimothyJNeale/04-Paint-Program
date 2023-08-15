from tkinter import *

root = Tk()
root.title("Paint")
root.geometry("800x800")
root.iconbitmap("01 Nenebiker.ico")

WIDTH = 600
HEIGHT = 400

# Create Canvas
my_canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
my_canvas.pack(pady=20)


root.mainloop()