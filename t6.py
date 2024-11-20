from tkinter import *

def func():
    print("Name : ",nameval.get(),"\nPhone : ",phoneval.get(),"\nGender : ",genderval.get(),"\nContact : ",contactval.get(),"\nPayment : ",paymentval.get(),"\nMeal : ",foodserviceval.get())

a = Tk()

a.geometry("600x500")
a.minsize(400,400)
a.maxsize(700,600)
a.title("Travell form using check box")

# Check box

Label(a,text="Welcome to Paraj Travells", font="comicsansms 13 bold").grid(column=3,pady=30)
name = Label(a,text="Name    : ")
phone = Label(a,text="Phone   : ")
gender = Label(a,text="Gender  : ")
contact = Label(a,text="Contact : ")
payment = Label(a,text="Payment : ")

name.grid(row=1,column=1)
phone.grid(row=2,column=1)
gender.grid(row=3,column=1)
contact.grid(row=4,column=1)
payment.grid(row=5,column=1)

nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
contactval = StringVar()
paymentval = StringVar()
foodserviceval = IntVar()

Entry(a,textvariable=nameval).grid(row=1,column=2)
Entry(a,textvariable=phoneval).grid(row=2,column=2)
Entry(a,textvariable=genderval).grid(row=3,column=2)
Entry(a,textvariable=contactval).grid(row=4,column=2)
Entry(a,textvariable=paymentval).grid(row=5,column=2)

# checkbox
foodservice = Checkbutton(text="Want to pre book your meals ? ",variable=foodserviceval)
foodservice.grid(row=6,column=2,pady=10)

Button(a,text="Submit",bg="orange",fg="white",padx=10,command=func).grid(row=7,column=2,padx=5)

a.mainloop()