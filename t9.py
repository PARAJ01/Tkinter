from tkinter import *

def paraj(event):
    print(f"Hello world at {event.x},{event.y}")
    

root = Tk()
root.geometry("600x400")
root.minsize(400,400)
root.maxsize(700,600)
root.title("Events handling")

widget = Button(root,text="Click me please !")
widget.pack()

widget.bind('<Button-1>',paraj)

# to exit for more info search on chrome tkinter event list
widget.bind('<Double-1>',quit)

root.mainloop()

