'''
Turples are lists that are immutable or not changeable onlike lists
'''

coordinates = (1, 2, 3)
# instead of 
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]


#Turple unpacking can also be used for lists too.
# better
# 0  1  2
x, y, z = coordinates

print(x)