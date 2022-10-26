from ast import Expression
from tkinter import N

# """""""
# Author: Omotoso David.
# purpose: Practice using Mathematical Expression.
# """"""
name = input(f'hi ! my friend, what is your name ? ')
age = int(input( name + f' how old are you '))
print( name + f' on your next birthday you will be {age + 1} years old.')
print(f'thank you for your time ' + name + ' i hope to see you next time.')

print()

carton = int(input(name + f' how many eggs cartons do you have? '))
print (name + f' you have {carton * 12} eggs ')
print(name + f' {carton * 12} is so much eggs can you give me one of the {carton * 12} eggs? ')
input(f'yes or no ')
print(name + f' thank you so much! see you next time.\n')



cookies = int(input(name + ' what is the number of cookies available'))
people  = int(input(name + f' how many people are there in the sitting room? '))
print(name + f' you will give each person {cookies / people} cookies')
print(name + 'You\'re such a kind boy')