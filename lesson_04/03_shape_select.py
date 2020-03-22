# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = 1200, 800
# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

print('Возможные фигуры:')
figures = ['треугольник', 'квадрат', 'пятиугольник', 'шестиугольник']
for key, value in enumerate(figures):
    print(f'{key}: {value}')

choice = int(input('Введите желаемую фигуру:'))
if choice not in range(0, 4):
    print('Вы ввели неправильно!')
    input()
choice = choice + 3

p = sd.get_point(500, 500)


def polygon(angle_num, point, angle=0, length=100):
    angle_n = 180 - round(((angle_num - 2) / angle_num), 15) * 180
    for i in range(angle_num):
        if i == angle_num - 1:
            sd.line(point, p, width=3)
            break
        v = sd.get_vector(start_point=point, angle=angle + i * angle_n, length=length, width=3)
        v.draw()
        point = v.end_point


polygon(choice, p)

sd.pause()
