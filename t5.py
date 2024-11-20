from tkinter import *

def getvals():
    print("Uservalue : ",uservalue.get())
    print("Password : ",passvalue.get())# .get will give value 

a = Tk()

a.geometry("600x500")
a.minsize(400,400)
a.maxsize(700,600)
a.title("Widget & Grind Layout")

# Widget & Grind Layout

# Variable classes in Tkinter
# boolean,double,int,String

user = Label(a,text = "User Name")
password = Label(a,text = "Password ")
user.grid()
password.grid(row=1)

# To take entry

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(a, textvariable=uservalue) # Entry is a widget
passentry = Entry(a, textvariable=passvalue)

userentry.grid(row = 0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvals,bg="orange",fg="white").grid()

a.mainloop()