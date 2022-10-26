from datetime import datetime

def main():


          pass
gender = input('Enter your gender (M or F): ')
birthdate = int(input('Enter your birthdate (YYYY-MM-DD): '))
heigth = float(input('Enter your height in inches: '))
weight = float(input('Enter your weight in U.S. inches: '))

def compute_age(birth_str):
          birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
          today = datetime.now()
          years = today.year - birthdate.year
          print(f'Age (years): {years}')
Age = compute_age(birthdate)


def kilo_frm_lb(pounds):
          lb = pounds / 0.45359237
          print(f'Weight (kg): {lb} ')
Kg = kilo_frm_lb(weight)


def inch_to_cm(inch):
          length = inch / 2.54
          return length
Length = inch_to_cm(heigth)


def body_mass_index(weight, height):
          mass = (10000 * weight) / (height * height)
          print(f'Body mass index: {mass}')

body_mass = body_mass_index(Kg,Length)


def basal_metabolic_rate(gender, weight, heigth, age):
          if gender == 'F':
                    bmr = 447.593 + 9.247 * weight + 3.098 * heigth - 4.330 * age
                    print(f'Basal metabolic rate (kcal/day): {bmr}')
          elif gender == 'M':
                    bmr = 88.362 + (13.397 * weight) + (4.799 * heigth) - (5.677 * age) 
                    print(f'Basal metabolic rate (kcal/day): {bmr}')

Bmr = basal_metabolic_rate(gender, Kg, Length, Age)
print(Age)
print(Kg)
print(Length)
print(Age)
print(body_mass)
print(Bmr)

