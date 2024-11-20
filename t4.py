from tkinter import *

a = Tk()

a.geometry("600x500")
a.minsize(400,400)
a.maxsize(700,600)
a.title("Buttons")

# creating func
def hello():
    print("Hello Buttons")

def one():
    print("Hello One")

f1 = Frame(a,borderwidth=3,bg="grey",relief=SUNKEN,padx=50)
f1.pack(side = LEFT,anchor="nw")

# Learning Buttons

b1 = Button(f1,fg="red",text = "Print now",borderwidth=3,relief=GROOVE,command=hello)
b1.pack(side = LEFT,pady=5)# by command print in cmd will done

b2 = Button(f1,fg="Blue",text = "Print one",borderwidth=3,relief=GROOVE,command=one)
b2.pack(side=LEFT,padx=5)

a.mainloop()