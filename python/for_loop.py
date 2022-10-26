
from operator import index, indexOf

#to print lists with their index number
lists = []
num = [2,7,3]
lists.append('yam')
lists.append('book')
lists.append('broom')
for e in range(len(lists)):
          print( lists[e], num[e])
          
# to print people in an array
# frind = ['david', 'joe D', 'Mayor'.upper()]
# for people in frind:
#           print(people)

# for index in range(6):
#           if index == 2:
#                     print('Second Iteration')
#           else:
#                     print('not second iteration')

for numbers in range(5, 25, 5):
          print(f'Number: {numbers}')