from tkinter import *
from tkinter import getint
root = Tk()
# creating a label widget 
mylabel = Label(root, text='HELLO WORLD').grid(row=1, column=0)
mylabel1 = Label(root, text='WORD CORRECTION / AUTOCOMPLETE APP').grid(row=0, column=0)

# Getting user Input
user_inpt = Entry(root, width=35, borderwidth=5)
# Design for the User input Box
user_inpt.grid(row=1, column=0, padx=20)

# Getting the user input and printing it on the screen
def myclick():
    mylabel = Label(root, text= user_inpt.get())
    mylabel.grid(row=3, column=0)

# Creating a button and designing the interface
myButton = Button(root, text='Check Word', padx=10, command=myclick, background='black', fg='white').grid(row=2, column=0)
# Positioning it on the screen
root.mainloop() 