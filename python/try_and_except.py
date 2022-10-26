number = int(input('Enter a number: '))
print(number)
# if the user mistakenly enters an alphabet, the programme will break so to avoid that,
# try and catch will be used
#catching and translating Error
try:
          value = 10/0
          number = int(input('Enter a number: '))
          print(number)
except ZeroDivisionError:
          print('Divided by zero')

# except ZeroDivisionError as err:
#           print(err)

except ValueError:
          print('Invalid input')
