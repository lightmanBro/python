
# friends = []
# friends.append(input('Type the name of a friend: '))
# friends.append(input('Type the name of a friend: '))
# friends.append(input('Type the name of a friend: '))
# friends.append(input('Type the name of a friend: '))
# print(f'Your friends are\n {friends[0]}\n {friends[1]}\n {friends[2]}\n {friends[3]}')



# friendNames = []
# friendsAge = []
# name = None
# age = None

# while name != '':
#           name = input('Type the name of a friend: ')
#           if name != '':
#                     friendNames.append(name)
# print()
# for friends in friendNames:
#           print(friends)






# friendNames.extend(friendsAge) # to add the elememts in friendsName to the elements in friendsAge.
# friends2 = friendNames.copy() # copyings the elements in friendsname and giving it to friends2

# friendsAge.pop(input('type name you want to remove: '))

# print(friendNames)


                                                  # TURPLE
#  EXAMPLES used for data that is not going to changed.
# turples items are not immuteable i.e coordinates[1] = 7 will give an error code and tell us that the object cannot be changed.
coordinates = (4,5) 
coordinates = [(5,6), (2,7), (3,8)]
          #      0, 1
print(coordinates[1])


# FUNCTION
def sayHi(names, aged):
          # print('hello' + names 'you are ' + str(aged) + '' )#turn number to string)



#RETURN KEYWORD
#           def cube(num):                                              
#                     num * num *num

# cube(3):                                           

          def cube(num):
                    return num * num *num
                    # anything under here will not be returned in the function
          result = cube(7)
          print(result)

# DICTIONARY
monthConversion = {
          # key     value
          'jan': 'January',
          'feb': 'February',
          'mar': 'March',
          'Apr': 'April',
}
print(monthConversion['jan'])
# or
print(monthConversion.get('jan', 'default value if the key value is not found inside the dictionary'))


#FOR LOOP

