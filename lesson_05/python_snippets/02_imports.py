# -*- coding: utf-8 -*-

# Способы импортирования кода

# Импорт всего модуля как имени в пространство имен текущего модуля

# Импорт всего модуля с другим именем (синонимом)
# чаще всего используется для сокращения
# или если в разных библиотеках есть модули с одинаковыми именами

# Можно импортировать конкретный элемент в пространство имен текущего модуля
from module_1 import function1, variable_1

function1()
print(variable_1)
# При таком импорте все равно выполняется весь пайтон-код импортируемого модуля

# Можно импортировать конктретный элемент с другим именем (синонимом)
from module_1 import function1 as f1, variable_1 as v1

f1()
print(v1)
# чаще всего используется если в разных модулях есть элементы с одинаковыми именами


###
# Импортировать все имена из модуля  в пространство имен текущего модуля
from module_1 import *


# Плохой стиль! потому что получается мешанина из собственных имен и имен в модуле
# и все зависит от того что было определено позже


def function1():
    print('Hey!')


from module_3 import *

function1()

###
# Python поставляется с библиотекой стандартных модулей
# полный список http://docs.python.org/3/library/index.html

import math

print(math.sin(90))

###
# Модули для импорта ищутся в текущем каталоге а затем в каталогах,
# указанных в переменной окружения PYTHONPATH, потом - в директории инсталляции пайтона

import my_math

print(my_math.cos(90))

# В действительности, поиск модулей производится в списке каталогов,
# передающемся в списке sys.path из модуля sys

import sys

for path in sys.path:
    print(path)


###
# Обычно все импорты указываются в начале модуля, но можно импортировать и в коде функций,
# тогда имена из модуля попадают в локальное пространство имен, в глобальном не видны.
# то есть import - вычислимый оператор

def some_func():
    from math import sin
    return sin(0)


print(some_func())
print(sin(0))
# под капотом: импорт выполяется один раз и хранится внутри пайтона,
# замедления при множественном вызове не происходит