# from tkinter import Canvas

''''
Omotoso David Omotola
week 4 Assignment.
'''''
from tkinter import *
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

import random

# border_color = Frame(background="red")

def main():
    scene_width = 800
    scene_height = 500

    canvas = start_drawing('Scene', scene_width, scene_height)
    # canvas = start_drawing(ran)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_line(canvas, 0, 30, 50, 30, width=5, fill="white")
    draw_line(canvas, 60, 30, 100, 30, width=5, fill="white")
    draw_line(canvas, 110, 30, 160, 30, width=5, fill="white")
    draw_line(canvas, 170, 30, 210, 30, width=5, fill="white")
    draw_line(canvas, 220, 30, 260, 30, width=5, fill="white")
    draw_line(canvas, 270, 30, 320, 30, width=5, fill="white")
    draw_line(canvas, 330, 30, 370, 30, width=5, fill="white")
    draw_line(canvas, 380, 30, 450, 30, width=5, fill="white")
    draw_line(canvas, 460, 30, 500, 30, width=5, fill="white")
    draw_line(canvas, 510, 30, 580, 30, width=5, fill="white")
    draw_line(canvas, 590, 30, 810, 30, width=5, fill="white")


#   draw_line(canvas, x0, y0, x1, y1, … xn, yn, width=1, fill="black"):
    draw_oval(canvas, 10, 480, 30, 500, fill="khaki1")
    draw_oval(canvas, 100, 450, 300, 530, fill="lightSkyBlue4")
    draw_oval(canvas, 280, 470, 370, 500, fill="lightSkyBlue2")

    draw_oval(canvas, 300, 450, 700, 530, fill="lightSkyBlue3")
    draw_oval(canvas, 500, 470, 570, 500, fill="lightSkyBlue1")
#   draw_oval(canvas, x0, y0, x1, y1, width=1, outline="black", fill="")

    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    ''' Draw the sky and all the objects in the sky'''
    draw_rectangle(canvas, 0, scene_height/4, scene_width, scene_height, width=0, fill='black')

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width,
                   scene_height / 3, width=0, fill='tan4')
    '''Draw Pine tree'''
    tree_center_x = 50
    tree_bottom = 100
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    '''Draw another Pine'''
    tree_center_x = 220
    tree_bottom = 100
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 400
    tree_bottom = 100
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 600
    tree_bottom = 165
    tree_height = 40
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 150
    tree_bottom = 165
    tree_height = 40
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    tree_center_x = 700
    tree_bottom = 150
    tree_height = 80
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    draw_rectangle(canvas, 0, 0, scene_width,
                   scene_height/8, width=0, fill='black')


def draw_pine_tree(canvas, center_x, bottom, height):
    ''' Draw a single Pine Tree
    Parameters
    canvas: the canvas where then function will draw a pine tree
    center_x, bottom: the x and y location in pixels where this function will draw the bottom of a pine tree.
    height: The height in pixels of the pine tree that this funcionn will draw.
    Return: Nothing'''

    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right,
                   bottom, outline='gray20', width=1, fill='tan3')

    skirt_width = height/2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_height / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top,
                 skirt_right, trunk_top,
                 skirt_left, trunk_top,
                 outline="gray20", width=1, fill="dark green")


main()
