'''
OMOTOSO DAVID OMOTOLA
'''


child_Meal = float(input(' what is price of a child\'s meal? '))
adult_Meal = float(input(' what is price of an adult\'s meal? '))
children_Count = float(input(' How many children are dinning? '))
adult_Count   = float(input(' How many adults are dinning? '))
tax_Rate     = float(input(' what is the tax rate? '))
print()
subtotal = (child_Meal * children_Count) + (adult_Count * adult_Meal)
print(f'Subtotal: ${subtotal}')
tax = subtotal / tax_Rate * .2
print(f'Sales Tax: ${tax:.2f}') 
total = subtotal + tax
print(f'Total: ${total:.2f}\n')

paymentAmount = float(input('What is the payment amount? '))
change = paymentAmount - total
print(f'Change: ${change:.3f}')

tip = total / 9
print(f'You can have ${tip:.2f} as your tip.\n')