# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (501, 501)
col = sd.COLOR_DARK_YELLOW
width = 1


def draw_brick(x, y):
    sd.line(sd.get_point(x, y), sd.get_point(x, y + 50), col, width)
    sd.line(sd.get_point(x, y + 50), sd.get_point(x + 100, y + 50), col, width)
    sd.line(sd.get_point(x + 100, y + 50), sd.get_point(x + 100, y), col, width)
    sd.line(sd.get_point(x + 100, y), sd.get_point(x, y), col, width)


i = 0
for y in range(0, 500, 50):
    for x in range(0, 1000, 100):
        if i % 2 == 0:
            draw_brick(x, y)
        else:
            draw_brick(x - 50, y)
    i += 1

sd.pause()
