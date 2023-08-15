from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import ImageGrab, Image, ImageDraw, ImageTk

root = Tk()
root.title("Paint")
root.geometry("800x800")
root.iconbitmap("01 Nenebiker.ico")

WIDTH = 600
HEIGHT = 400

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

# Save image
def save_as_png():
    result = filedialog.asksaveasfilename(initialdir='c:', filetypes=(("png files", "*.png"), ("all files", "*.*")))
    if result.endswith(".png"):
        pass
    else:
        result += ".png"

    if result:
        x = root.winfo_rootx() + my_canvas.winfo_x()
        y = root.winfo_rooty() + my_canvas.winfo_y()
        x1 = x + my_canvas.winfo_width()
        y1 = y + my_canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(result)



# Create Canvas
my_canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
my_canvas.pack(pady=20)

brush_color = "black"
bg_color = "white"

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

# Program options frame
options_frame = LabelFrame(brush_options_frame, text="Program Options")
options_frame.grid(row=0, column=3, padx=50)

# Clear screen button
clear_button = Button(options_frame, text="Clear Screen", command=lambda: my_canvas.delete(ALL))
clear_button.pack(padx=10, pady=10)

# Save image button
save_image_button = Button(options_frame, text="Save to PNG",command=save_as_png)
save_image_button.pack(padx=10, pady=10)

root.mainloop()