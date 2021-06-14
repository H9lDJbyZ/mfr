# -*- coding: utf-8 -*-

import simple_draw as draw


draw.resolution = (1200, 600)

x = 100
y = 100
radius = 50
point = draw.get_point(x, y)
for _ in range(3):
    radius += 5
    draw.circle(point, radius, width=2)


def bubble(point, step, color=draw.COLOR_YELLOW):
    radius = 50
    for _ in range(3):
        radius += step
        draw.circle(point, radius, color, 2)


# Нарисовать 10 пузырьков
draw.clear_screen()
for x in range(100, 1001, 100):
    point = draw.get_point(x, 100)
    bubble(point, 4)

# Нарисовать три ряда по 10 пузырьков
draw.clear_screen()
for x in range(100, 1001, 100):
    for y in range(100, 301, 100):
        draw.start_drawing()
        point = draw.get_point(x, y)
        bubble(point, 4)
        draw.finish_drawing()

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
draw.clear_screen()
for _ in range(100):
    draw.start_drawing()
    point = draw.random_point()
    bubble(point, 3, draw.random_color())
    draw.finish_drawing()



draw.pause()
