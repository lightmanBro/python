'''
Omotoso David week 13 Prove Assignment
'''
temp_input = int(input('What is the temperature?: '))
temp_type = input('Farenhite or Celcius? F/C: ')

def calc_chill(speed, temp):
          chill = 35.74 + 0.6215 * temp - 35.75 * speed ** 0.16 + 0.4275 * temp * speed ** 0.16
          return chill

def convert_to_f(temp):
          return  (temp * (9/5)) + 32
          
if temp_type.lower() == 'f':
          for number in range(5, 65, 5):
                    speed = number
                    chill = calc_chill(speed, temp_input)
                    print(f'At temperature {temp_input}.0F, And wind speed {speed}mph, the windchill is {round(chill, 3)}')

# for number in range(5, 65, 5):
#                     speed = number
# chill = calc_chill(speed, temp_input)
          
if temp_type.lower() == 'c':
          for number in range(5, 65, 5):
                    speed = number
                    temp = convert_to_f(temp_input)
                    windchill = calc_chill(speed,temp)
                    print(f'At temperature {temp_input}.0F, And wind speed {speed}mph, the windchill is {round(windchill, 3)}')