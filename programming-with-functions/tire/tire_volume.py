from datetime import datetime
''''
Gets the current date from the computer's operating system.
Opens a text file named volumes.txt for appending.
Appends to the end of the volumes.txt file one line of text that contains the following five values:
current date
width of the tire
aspect ratio of the tire
diameter of the wheel
volume of the tire

Find tire prices for four or more tire sizes online. Add a set of if … elif … else statements in your program that use the tire width, tire aspect ratio, and wheel diameter that the user enters to find a price and then print the price.
          After your program prints the tire volume to the terminal window, your program should ask the user if she wants to buy tires with the dimensions that she entered. If the user answers "yes", your program should ask for her phone number and store her phone number in the volumes.txt file.
'''''
import math

w = int(input('Enter the width of the tire in mm (ex 205): '))
a = int(input('Enter the aspect ratio of the tire (ex 60): '))
d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

v = math.pi * w*w *a*(w*a + 2540 * d)
result = v/ 10000000000

current_date_and_time = datetime.now()
dt = f"{current_date_and_time:%Y-%m-%d}"
print(f' {dt}, {w}, {a}, {d},  {result:.2f}')


with open('C:/Users/user/Desktop/python/programming-with-functions/tire/volume.txt', 'at') as volume:
          print(f' {dt}, {w}, {a}, {d},  {result:.2f}', file=volume)

tire_price = 0
if w in range(185, 205) and a in range(45, 60) and d in range(15, 20):
          tire_price = 155
          print(f'The volume of the tire is {result:.2f} liters and the price of the tire is ${tire_price} ')
elif w in range(150, 180) and a in range(30, 45) and d in range(11, 15):
          tire_price = 115
          print(f'The volume of the tire is {result:.2f} liters and the price of the tire is ${tire_price} ')

user_ques = input('Do you wish to purchase the Tyre you searched for? Y/N: ')
if user_ques == 'Y':
          name = input('Please tell us your name: ')
          phone = input('Please Enter your phone number: ')
          with open('C:/Users/user/Desktop/python/programming-with-functions/tire/volume.txt', 'at') as volume:
                    print(f' {name} wants to buy tire, phone number is {phone}', file= volume)
else:
          print('Thank you! we hope to do business with you someday.')
