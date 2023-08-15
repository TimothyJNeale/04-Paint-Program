from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser

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

brush_color = "black"
bg_color = "white"

def paint(e):
    # Brush params
    #brush_width = 25

    #brush_type = BUTT
    # BUTT, ROUND, PROJECTING

    # Create a red line following the mouse pointer
    my_canvas.create_line(e.x-1, e.y-1, e.x+1, e.y+1, 
                          capstyle=brush_type.get(),
                          fill=brush_color, 
                          width=int(brush_slider.get()), 
                          smooth=True)
    
# Change the brush size
def change_brush_size(thing):
    brush_slider_label.config(text=int(brush_slider.get()))

# Change brush color
def change_brush_color():
    global brush_color
    brush_color = colorchooser.askcolor(color=brush_color)[1]
    

# Change canvas background color
def change_canvas_color():
    global bg_color
    bg_color = colorchooser.askcolor(color=bg_color)[1]
    my_canvas.config(bg=bg_color)

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

# Brush type
brush_type_frame = LabelFrame(brush_options_frame, text="Brush Type", height=400)  # LabelFrame is a frame with a label
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set("round")

# Create radio buttons for brush type
brush_type_radio1 = Radiobutton(brush_type_frame, text="Round", variable=brush_type, value="round")
brush_type_radio2 = Radiobutton(brush_type_frame, text="Slash", variable=brush_type, value="butt")
brush_type_radio3 = Radiobutton(brush_type_frame, text="Diamond", variable=brush_type, value="projecting")

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# Change colors
change_colors_frame = LabelFrame(brush_options_frame, text="Change Colors")
change_colors_frame.grid(row=0, column=2)

# Change brush color button
brush_color_button = Button(change_colors_frame, text="Brush Color", command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

# Change canvas background color
canvas_color_button = Button(change_colors_frame, text="Canvas Color", command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)


root.mainloop()