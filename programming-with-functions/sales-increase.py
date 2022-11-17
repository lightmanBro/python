
''''
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest sales days. On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.
'''
from datetime import datetime


subTotal = 0
discount_amount = 0
six_percentage = 0
current_date_and_time = datetime.now()
day_of_the_week = current_date_and_time.weekday()

while subTotal != 0:
          subTotal = float(input('What is the subtotal of your purchases? '))
          # sales_tax = float(input('What is the sales tax? '))
          if subTotal >= 50 & day_of_the_week == 1 | 2:
                    # discount_amount = subTotal * 10 / 100
                    # six_percentage = (subTotal - discount_amount) * 6 / 100
                    # print(f'your total amount is {six_percentage}')
                    print(subTotal)