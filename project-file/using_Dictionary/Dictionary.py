customer = {
          'name': 'John smith',
          'age': 30,
          'is Verified': True
}

# using the .get() method to get Properties fromm the dictionary 
# the get method is udeful so that the programme will now throw NONE rather than an error message.

print(customer.get('birthdate')) 

#adding values to the customer
customer['birthdate'] = 'jan 1 1982'
print(customer)

'''
Examples of dictionary Usefullness:
translating digits to words
'''
phone = input('Phone: ')
digits_mapping = {
          '1': 'One',
          '2': 'Two',
          '3': 'Three',
          '4': 'Four',
          '5': 'Five',
          '6': 'Six'
}
output = ''
for ch in phone:
          output += digits_mapping.get(ch, '!')