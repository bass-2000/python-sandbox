# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(num_sides):
    def draw_shape(point, length, angle):
        delta = 360 // num_sides
        sum_angle = 360 + angle
        for current_angle in range(angle, sum_angle, delta):
            point = sd.vector(start=point, angle=current_angle, length=length, width=4)

    return draw_shape


sd.start_drawing()
draw_triangle = get_polygon(num_sides=3)
draw_triangle(point=sd.get_point(150, 150), angle=60, length=100)
draw_square = get_polygon(num_sides=4)
draw_square(point=sd.get_point(400, 150), length=70, angle=90)
draw_pentagon = get_polygon(num_sides=5)
draw_pentagon(point=sd.get_point(150, 300), length=70, angle=108)
draw_hexagon = get_polygon(num_sides=6)
draw_hexagon(point=sd.get_point(400, 300), length=70, angle=120)
sd.finish_drawing()

sd.pause()
