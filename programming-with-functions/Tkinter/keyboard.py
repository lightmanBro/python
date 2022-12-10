from tkinter import *
from tkinter import ttk
import time
"""_summary_ To create anything in tkinter you will have to create the widget first then add it to th screen
    """
screen = Tk()
# Creating a labe;l and adding it to the screen
myLabel = Label(screen, text='hello world')
screen.geometry('600x400+50+50')
screen.title('Word Completion App')
myLabel.pack()
# Entry Box
userInpt = Entry(screen)
userInpt.pack()
# Function to get the text from the .txt file and print it to the screen
def printScreen():
    # time.sleep(.02)
    printSpace = Label(screen, text='Clicked a button')
    printSpace.pack()
    
# Storing the file directory in a variable
file = 'programming-with-functions\Tkinter\words.txt'
# creating a function to read the txt file and turn it to a list.
def readFromTxt():
    with open(file,'rt') as wordContainer:
        return wordContainer
    
def checkWord(wordContainer):
    dictionary = []
    for words in wordContainer:
            firstComma = words.rindex(' ' + 1)
            commaList = words.replace(firstComma, ',')
            dictionary.append(commaList)
            if len(userInpt.get()) > 3 in dictionary:
                # printSpace = Label(screen, text= userInpt)
                # printSpace.pack()
                print(dictionary)


def exit():
    import sys; sys.exit()
    
printBtn = Button(command=readFromTxt, text='Check word')
printBtn.pack()
exbtn = Button(command=exit, text='Exit')
exbtn.pack()
screen.mainloop()