# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint, choice

ENLIGHTENMENT_CARMA_LEVEL = 777

ENLIGHTENMENT_CARMA_LEVEL = 777
total_amount_karma = 0


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class DepressionError(Exception):
    pass


class GluttonyError(Exception):
    pass


class SuicideError(Exception):
    pass


karma_events = [IamGodError, DrunkError, CarCrashError, DepressionError, GluttonyError, SuicideError]


def one_day():
    amount_karma = randint(1, 7)
    dice = randint(1, 13)
    if dice == 13:
        evil_event = choice(karma_events)
        raise evil_event
    return amount_karma


while total_amount_karma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        total_amount_karma += one_day()
    except IamGodError:
        print('Godlike')
    except DrunkError:
        print('I\'m ok')
    except CarCrashError:
        print('Too fast ...')
    except DepressionError:
        print('I know that feel, bro')
    except GluttonyError:
        print('ATTENTION! Calories attack')
    except SuicideError:
        print('Good bye pretty world')
