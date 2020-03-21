# -*- coding: utf-8 -*-

import random

import simple_draw as sd

sd.resolution = (1200, 600)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 50
    # Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=sd.random_color())


# Нарисовать три ряда по 10 пузырьков
# for y in range(100, 301, 100):
#     # Нарисовать 10 пузырьков в ряд
#     for x in range(100, 1001, 100):
#         point = sd.get_point(x, y)
#         bubble(point, 5)
#         bubble(point, 5)
#         bubble(point, 5)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    step = random.randint(3, 10)
    bubble(point, step)

sd.pause()
