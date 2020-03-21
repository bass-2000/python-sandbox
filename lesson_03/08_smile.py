# -*- coding: utf-8 -*-

import random

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

sd.resolution = (1200, 600)
colors = (sd.COLOR_CYAN, sd.COLOR_GREEN, sd.COLOR_YELLOW, sd.COLOR_RED, sd.COLOR_PURPLE, sd.COLOR_ORANGE)


def draw_smile(x, y, col):
    coor1 = sd.get_point(x, y)
    coor2 = sd.get_point(x + 150, y + 100)
    eye1 = sd.get_point(x + 40, y + 60)
    eye2 = sd.get_point(x + 100, y + 60)
    mouth_line1 = sd.get_point(x + 40, y + 20)
    mouth_line2 = sd.get_point(x + 70, y + 15)
    mouth_line3 = sd.get_point(x + 100, y + 20)
    sd.ellipse(coor1, coor2, col, 2)
    sd.circle(eye1, 10, col, 2)
    sd.circle(eye2, 10, col, 2)
    sd.line(mouth_line1, mouth_line2, col, 2)
    sd.line(mouth_line2, mouth_line3, col, 2)


for _ in range(0, 100):
    draw_smile(int(random.uniform(0, 1000)), int(random.uniform(0, 500)), colors[int(random.uniform(0, 5))])
sd.pause()

sd.pause()
