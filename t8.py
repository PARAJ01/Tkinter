from tkinter import *

a  = Tk()

canvas_width = 600
canvas_height = 400

a.geometry(f"{canvas_width}x{canvas_height}")
a.title("Canvas widget")

# Canvas widget in python

can_widget = Canvas(a,width=canvas_width,height=canvas_height)
can_widget.pack()

# The line goes from the point x1,y1 to x2,y2 goes to 4th quadrant
can_widget.create_line(0,30, 600,30,fill="red",width=3)
can_widget.create_line(30,0, 30,400,fill="magenta",width=5)

# top left , bottom right
can_widget.create_rectangle(40,40,300,200,fill="blue")

# center co of text
can_widget.create_text(400,300,text="Paraj")

# 4 point will be of any rectangle if want circle give co of a square
can_widget.create_oval(40,40,300,200,fill="white")


a.mainloop()