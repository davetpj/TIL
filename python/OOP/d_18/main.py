from turtle import Turtle


def draw_star:

# def draw_sqpolygon(x, y):
#     pass
#
#
# radius = 150
# x = -150
# y = -150
# for _ in range(6):
#     print(radius)
#     draw_sqpolygon(x, y)
#
#     x += radius
#     radius /= 2
#     x += radius
#     y += radius
#     print(x, y)
#
# def draw_sqpolygon(pen, x, y, radius, size=1, side=None, pen_color='black', fill_color=None):
#     pen.pensize(size)
#     pen.pencolor(pen_color)
#
#     pen.penup()
#     pen.goto(x, y)
#     pen.pendown()
#
#     if not fill_color:
#         pen.circle(radius, steps=side)
#     else:
#         pen.fillcolor(fill_color)
#         pen.begin_fill()
#         pen.circle(radius, steps=side)
#         pen.end_fill()
#
#
# my_pen = Turtle()
#
# floor = 1
# reverse_range = [7, 6, 5, 4, 3, 2, 1]
# y_position = -300
# for i in reverse_range:
#     if floor % 2 != 0:
#         start_color = 'red'
#         else_color = 'blue'
#         side = None
#     else:
#         start_color = 'blue'
#         else_color = 'red'
#         side = 4
#     x_position = -300
#     for _ in range(i):
#         if _ % 2 == 0:
#             draw_sqpolygon(pen=my_pen, x=x_position, y=y_position, radius=40, size=1, side=side, pen_color='black',
#                            fill_color=start_color)
#         else:
#             draw_sqpolygon(pen=my_pen, x=x_position, y=y_position, radius=40, size=1, side=side, pen_color='black',
#                            fill_color=else_color)
#         x_position += 90
#     y_position += 90
#     floor += 1
#
#
#

# my_pen.shape("turtle")
# my_pen.penup()
# my_pen.left(180 + 45)
# my_pen.forward(450)
# my_pen.left(90 + 45)
#
#
# floor = 1
# abc = [7, 6, 5, 4, 3, 2, 1]
#
#
# for i in abc:
#     if floor % 2 != 0:
#         start_color = 'red'
#         else_color = 'blue'
#     else:
#         start_color = 'blue'
#         else_color = 'red'
#
#     for _ in range(i):
#         my_pen.color('black')
#         if _ % 2 == 0:
#             my_pen.fillcolor(start_color)
#         else:
#             my_pen.fillcolor(else_color)
#
#         my_pen.begin_fill()
#
#         my_pen.pendown()
#         if floor % 2 != 0:
#             my_pen.circle(40)
#         else:
#             my_pen.circle(40, steps=4)
#         my_pen.penup()
#
#         my_pen.end_fill()
#         my_pen.forward(90)
#
#     my_pen.left(90)
#     my_pen.forward(90)
#     my_pen.left(90)
#     my_pen.forward(90 * i)
#     my_pen.left(180)
#
#     floor += 1
#
