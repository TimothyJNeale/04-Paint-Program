from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Paint")
root.geometry("800x800")
root.iconbitmap("01 Nenebiker.ico")

WIDTH = 600
HEIGHT = 400

# Create Canvas
my_canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
my_canvas.pack(pady=20)

# # Create a line
# x1, y1, x2, y2 = 0, 100, 300, 100
# my_canvas.create_line(x1, y1, x2, y2, fill="red")

# # Create another line to cross the first
# x1, y1, x2, y2 = 100, 0, 100, 300
# my_canvas.create_line(x1, y1, x2, y2, fill="red")


def paint(e):

    # Brush params
    #brush_width = 25
    brush_color = "green"
    brush_type = BUTT
    # BUTT, ROUND, PROJECTING

    # Create a red line following the mouse pointer
    my_canvas.create_line(e.x-1, e.y-1, e.x+1, e.y+1, 
                          capstyle=brush_type, 
                          fill=brush_color, 
                          width=int(brush_slider.get()), 
                          smooth=True)
    
# Change the brush size
def change_brush_size(thing):
    brush_slider_label.config(text=int(brush_slider.get()))



# Bind the mouse to the Canvas
my_canvas.bind("<B1-Motion>", paint)

# Create brush options frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# Brsh size
brush_size_frame = LabelFrame(brush_options_frame, text="Brush Size")  # LabelFrame is a frame with a label
brush_size_frame.grid(row=0, column=0, padx=50)

# Brush slider
brush_slider = ttk.Scale(brush_size_frame, from_=1, to=100, 
                         command=change_brush_size, 
                         orient=VERTICAL,
                         value=10)
brush_slider.pack(pady=10, padx=10)

# Brush slider label
brush_slider_label = Label(brush_size_frame, text=brush_slider.get())
brush_slider_label.pack(pady=5)


root.mainloop()