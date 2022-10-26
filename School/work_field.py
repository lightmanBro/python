
from itertools import count

print('HI! YOU ARE WELCOME TO THE WORLD LIFE EXPECTANCY LISTS')
exp_list = []
country_list = []
key_wrd = []
year  = []
max_exp = -1
min_exp = 1000
min_year = 5000
max_year = 0
max_country = ''
min_country = ''
average = []

# For the User-inputs
user_min_exp = 5000
user_max_exp = 0
user_max_country = ''
user_min_country = ''
average_country = ''
user_ques = int(input('Enter the year of interest: '))

# with open('School/reading_files/life-expectancy.csv') as life_expextancy:
with open('School/reading_files/life-expectancy.csv') as life_expextancy:

        next(life_expextancy)

        for line in life_expextancy:
               parts = line.split(',')
               line = line.strip()
               country = parts[0]
               keywrd = parts[1]
               years = int(parts[2])
               expectancy = float(parts[3])

               exp_list.append(expectancy)
               country_list.append(country)
               key_wrd.append(keywrd)
               year.append(years)


for index in range(len(exp_list)):
        exp = exp_list[index]
        countr = country_list[index]
        yr = year[index]



        if exp > max_exp:
                max_exp = exp
                max_country = countr
                max_year = yr

        if exp < min_exp:
                min_exp = exp
                min_country = countr
                min_year = yr

print(f'The country with the maximum life expectancy is {max_country} with {max_exp} in {max_year}')
print(f'The country with the minimum life expectancy is {min_country} with {min_exp} in {min_year}\n\n')

for index in range(len(exp_list)):
        exp = exp_list[index]
        countr = country_list[index]
        yr = year[index]
        average.append(exp_list[index])
        average_exp = sum(average) / len(average)

        if exp > user_max_exp and yr == user_ques:
                user_max_exp = exp
                user_max_country = countr
                


        if exp < user_min_exp and yr == user_ques:
                user_min_exp = exp
                user_min_country = countr


print(f'for the year {user_ques}')
print(f'The the average life expectancy across all countries in {user_ques} is {average_exp}')
print(f'The maximum life expectancy in {user_ques} was in {user_max_country} with {user_max_exp}')
print(f'The min life expectancy in {user_ques} was in {user_min_country} with {user_min_exp}')