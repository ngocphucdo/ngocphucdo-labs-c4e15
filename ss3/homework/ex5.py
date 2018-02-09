from turtle import *

def draw_star(x ,y, length):
    goto(x ,y)
    for i in range(5):
        forward(length)
        right(144)
        forward(length)
draw_star(0, 0, 100)
