"Omotoso David"
"week 5"
"simple Grading Calculator"


# EXAMPLE 1
print('Welcome my friend, It seems you want to know your grade? ')
name = input('what is your name ')
print(name + ' what is your score')
score = float(input('Write your score here '))
if score >= 95 and score == 100:
          print(name + 'Excellent! Your grade is A')
elif score >= 90 and score < 95:
          print(name + ' Your grade is A-')
elif score >= 85 and score < 90:
          print(name + ' your grade is B+')
elif score >= 75 and score < 85:
          print(name + ' Your grade is B')
elif score >= 70 and score < 75:
          print(name + ' Lucky you! your grade is C')

elif score < 70 and score >= 65:
          print(name + ' You passed this course on probabtio')
else:
          print(name + ' Sorry you will have to take this course again \n' 'i wish you best of luck' )


# EXAMPLE 2
name = input('what is your name ')
grade = int(input( name + 'what is your grade '))
if grade >= 90:
          letter = 'A'
elif grade >= 80:
          letter = 'B'
elif grade >= 70:
          letter = 'C'
elif grade >= 60:
          letter = 'D'
else:
          letter = 'F\n'

print(name + ' your grade is: {letter}')

if grade >= 70:
          print(name + ' congratulations!! You passed the corse')
else:
          print(name + ' sorry you will have to try harder next term')

