# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x = randint(50, sd.resolution[0])
        self.y = randint(sd.resolution[1], sd.resolution[1] * 1.5)
        self.length = randint(10, 80)

    def __str__(self):
        return 'Snowflake: x = {}, y = {}, length = {}'.format(self.x, self.y, self.length)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def move(self):
        self.x += randint(-10, 10)
        self.y -= randint(10, 20)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.COLOR_WHITE)

    def can_fall(self):
        return self.y < -self.length


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


def get_flakes(count=2):
    additional_flakes = []
    for i in range(count):
        flake_0 = Snowflake()
        additional_flakes.append(flake_0)
    return additional_flakes


def get_fallen_flakes(data):
    print(flakes)
    for element in data:
        if element.can_fall():
            data.remove(element)
            print("data", data)
        return data


flakes = get_flakes(count=30)

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
while True:
    sd.start_drawing()
    quantity = 0
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    for flake in flakes:
        if flake.can_fall():
            flakes.remove(flake)
            quantity += 1

    new_flakes = get_flakes(count=quantity)
    flakes.extend(new_flakes)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
