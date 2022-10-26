
def main():
    pass
start = float(input('What is your start mile? '))
end = float(input('What is your end mile? '))
fuel_amount = float(input('How many gallon of fuel was used? '))

def miles_per_gallon(start_miles, end_miles, amount_gallons):
          miles = end_miles - start_miles
          mile_per_gallon = miles / amount_gallons

          return mile_per_gallon

result = miles_per_gallon(start, end, fuel_amount)
print(f'{result:.1f} miles per gallon')

def lp100k_from_mpg(mpg):
         conversion = 235.215 / mpg
         return conversion
miles_per_g = lp100k_from_mpg(result)

print(f'{miles_per_g:.2f}')

main()