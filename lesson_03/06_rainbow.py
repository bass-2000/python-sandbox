# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# sd.resolution = (1200, 600)
# y1 = 100
# y2 = 500
# coor1 = sd.get_point(100, y1)
# coor2 = sd.get_point(500, y2)
# delta = 10
# i = 0

# for i in range (7):
#    coor1 = sd.get_point(100, y1)
#    coor2 = sd.get_point(500, y2)
#    y1 -= delta
#    y2 -= delta
#    sd.line(coor1, coor2, rainbow_colors[i], 10)


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

y = 0

for color in rainbow_colors:
    center_point = sd.get_point(300, y)
    sd.circle(center_point, 500, color, 20)
    y -= 20

sd.pause()
