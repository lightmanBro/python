#Area of square#
square_side = float(input(f'what is the length of a square  '))
area = square_side **2
print(f'the area of the square is {area}\n')

#Area of rectangle#
rectangle_length = float(input(f'what is the length of rectangle? '))
rectangle_width = float(input(f'what is the width of rectangle? '))
rect_area = rectangle_length * rectangle_width
print(f'the area of the rectangle is {rect_area} \n')

#radius of circle#

circle_rad = float(input(f'what is the radius of the circle? '))
radius = 3.14 * (circle_rad **2)
print(f'the radius of the circle is {radius}\n')


import math

rad_circ = float(input(f'what is the radius of the circle? '))
ans_circ = math.pi * (rad_circ **2)
print(f'the area of the circle is {ans_circ}\n')

