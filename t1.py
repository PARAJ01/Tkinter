from tkinter import *
from PIL import Image, ImageTk
a_root = Tk()

# gui logic here
a_root.geometry("500x500") # width x height sets frame size
a_root.minsize(200,100) # width , height : locks minimum size
a_root.maxsize(400,400)
#-----------------------------------------------------------------------------------------------
b = Label(text = "Paraj is a good boy")
b.pack()
#------------------------------------------------------------------------------------------------
# for jpg images
image = Image.open("download.png")
photo1 = ImageTk.PhotoImage(image)
d = Label(image = photo1)
d.pack()
# for png images
photo = PhotoImage(file = "a1.png")
c = Label(image = photo)    # write in terminal 'pip install pillow'
c.pack()
#----------------------------------------------------------------------------------------------

a_root.mainloop()