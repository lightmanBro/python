'''
Understanding Functions and its methods and Properties
'''

def greet_user():       
          print('Hi there')
          print('Welcome Abroad')


print('start')
greet_user()
print('stop!')

'''
function Parameters
'''
def greet_user(first_name, last_name):

          print(f'Hi {first_name} {last_name}')
          print('Welcome Abroad')
          
greet_user(
first_name = input('First Name: '),
last_name = input('Last name: '))

'''
keyword Argument:
always use the positional arguements but for functions that has a lot of parameters and for readability it is good to use keyword arguments
'''
# for easy readability and not to worry about the arrangement of the Arguements 
greet_user(first_name='David', last_name='busch')
# Use positional argument before using keyword argument.
greet_user('David', last_name='busch')

# Example for readability: 
calc_cost(50, 5, 0.1)
calc_cost(total=50, shipping=5, tax=0.1)