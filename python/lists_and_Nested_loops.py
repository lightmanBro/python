#   2D LISTS AND NESTED FOR LOOP

#list in lists
number_grid = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [0]
]
print(number_grid[0][2])
print(number_grid[2][2])
#USING FOR LOOP
for row in number_grid:
          print(row)
for row  in number_grid:
          for col in row:
                    print(col)

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
          print('x' * x_count)


'''
getting maximum number
'''
numb = [3, 6, 2, 7, 8, 5, 10]
max = numb[0]
for  number in numb:
          if number > max:
                    max = number
print(max)

'''
Removing duplicates in a list
'''
duplicates = [2,2,4,6,3,6,4,1]
uniqes = []
for number in duplicates:
          if number not in uniqes:
                    uniqes.append(number)
print(uniqes)

'''
working with lists methods
adding a number : .append()
adding a number to a specific position : .insert(2,(index), 3(object))
removing: .reomve()
clearing the list: .clear()
removing the last item : .pop()
checking for the existense of an item:
 .indexOf()
 print(items in lists).

counting the amount of a specific elements in list: 
 print(lists.count(items))
sorting items :
lists.sort() >> print(list)
to copy : lists.copy() >> list2 = list.copy()
'''
