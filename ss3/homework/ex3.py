from turtle import *
def draw_square(l, cl):
    # l = 100
    # cl = 'red'
    pencolor(cl)
    for i in range(4):
        forward(l)
        left(90)

draw_square(100, 'red')
