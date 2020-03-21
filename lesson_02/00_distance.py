#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

def func(tuplea, tupleb):
    return ((tuplea[0] - tupleb[0]) ** 2 + (tuplea[1] - tupleb[1]) ** 2) ** 0.5


distances = {}
for keyA in sites:
    for keyB in sites:
        if (keyA != keyB):
            distances[keyA + '-' + keyB] = str(func(sites[keyA], sites[keyB]))

print(distances)
