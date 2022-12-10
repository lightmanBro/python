import asyncio
from tkinter import *
from tkinter import ttk
import asyncio
import sys
import time
word = ''
words = ['bank', 'troops', 'maker', 'outcast', 'bake', 'bankole']
user_inpt = input('Enter word ')
# start = time.sleep(0.3)


def display_message():
    for word in words:
        if user_inpt in word:
            print(word)
            # sys.stdout.write(word+ ' ')
            # sys.stdout.flush()
            # time.sleep(delay)
display_message()
# button = Button(command=display_message)
# button.pack(pady=30)
# async def hello():
#         await asyncio.sleep(0.1)
#         if len(user_inpt) >= 3:
#             button.invoke()
# asyncio.run(hello())
# # button.invoke()

