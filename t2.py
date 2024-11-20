from tkinter import *
from PIL import Image, ImageTk

a = Tk()
a.geometry("600x550")
a.minsize(300,200)
a.maxsize(600,600)
a.title("First  Paraj  GUI  (^ _ ^)")
# Gui logic here
# Important Label Option
"""text - adds the Text
bg - background
fg - foreground
font - sets the font
1 : font = ("comicsansms",13,"bold")
2 : font = "comicsansms 13 bold"
padx - x padding
pady - y padding
relief - border styling - SUNKEN , RAISED,GROOVE,RIDGE"""

title_label = Label(text = "We will learn here label option and gui logic", 
                    bg = "black",fg = "yellow",padx = 23,pady = 23, 
                    font = "comicsansms 13 bold", borderwidth=6,relief=SUNKEN)

# Important pack options
# anchor = nw
# side = top , bottom , left , right
# fill
# padx
# pady
title_label.pack(side = "right",anchor="sw",fill=Y,padx = 30,pady = 30)# north west

a.mainloop()