
import tkinter as tk
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.label(frm, Text='Hello world').grid(column=0, row=0)
ttk.Button(frm, text='Quit', command=root.destroy).grid(column=1, row=0)
root.mainloop()