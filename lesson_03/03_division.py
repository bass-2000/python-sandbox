# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 5, 2
finalA = a
q = 0
while a >= b:
    a -= b
    q += 1
print('Целочисленное деление', finalA, 'на', b, 'дает', q)