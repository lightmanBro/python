'''
Defining a function and giving it a return statement is usefull when the function being defined has a lot of lines of code and we want to store the function in a variable before using it so as to use the variable later in the program.
By default all the functions in python returns NONE
 if a return stattement is not given the code will not work as planned, though print() can be used to view the value in the terminal.
'''

from email import message
from unittest import result


def square(number):
          return number * number

def emoji_converter(message):
          words = message.split(' ')
          emojis = {
                    ':)': '😀',
                    '(:': '😔'
          }
          output = ''
          for word in words:
                    output += emojis.get(word, word) + ' '
          return output


message = input('>')
result = emoji_converter(message)
print(message)