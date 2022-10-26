'''
CLASS: a class is a blueprint foundation on which hundreds of objects derive their structure from.
OBJECT: an instance of a class which can be as many as possible and can have unique Attributes inside each of them.
'''
# Example 1
class Point:
          #Constructor function to give the objects parameters.
          #just as the (this.) object in javaScript
          def __init__(self, x, y):
                    self.x = x 
                    self.y = y


          def move(self):
                    print('move')

          def draw(self):
                    print('Draw')


#Object
point1 = Point(10, 12)
point1.draw()
point1.move()
#Object Attributes
point1.x = 10
point1.y = 30
# print(point1(10,15))



# point2 = Point()
# point2.name = 'second Point'
# point2.age = 6
# point2.x = 69
# point2.y = 15
# print(point2(2,7))

# # Calling the constructor function#
point = Point(10,15)
print(point)


# # Example 2

# class Person:
#           def __init__(self, name):
#                     self.name = name

#           def talk(self):
#                     print(f'Hi, i am {self.name}')


# david = Person('David Guy')
# print(david.name)
# david.talk()