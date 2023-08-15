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

# Create a line
x1, y1, x2, y2 = 0, 100, 300, 100
my_canvas.create_line(x1, y1, x2, y2, fill="red")

# Create another line to cross the first
x1, y1, x2, y2 = 100, 0, 100, 300
my_canvas.create_line(x1, y1, x2, y2, fill="red")

root.mainloop()