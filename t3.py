from tkinter import *
a = Tk()

a.geometry("655x333")
a.minsize(300,300)
a.maxsize(700,700)
a.title("Second GUI by Paraj")
# Learning Frames

f1 = Frame(a,bg = "grey",borderwidth=6,relief=SUNKEN)
f1.pack(side = LEFT,fill="y",pady=32)# by these 32 space is there in y axis

f2 = Frame(a,bg="grey",borderwidth=7,relief=GROOVE)
f2.pack(side = TOP,fill="x")
# Logic here
l1 = Label(f1,text= "Minecraft : A endless game\n1 : Villager\n2 : Steve",bg="grey",fg="black",
           font="comicsansms 10 bold",pady=300)
l1.pack(pady=50)

l2 = Label(f2,text="Welcome !",bg = "grey",fg="white", padx=50) # white space of lable padding
l2.pack()

a.mainloop()