from turtle import *

def draw_star(x ,y, length):
    goto(x ,y)
    for i in range(5):
        forward(length)
        right(144)
        forward(length)
draw_star(0, 0, 100)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
