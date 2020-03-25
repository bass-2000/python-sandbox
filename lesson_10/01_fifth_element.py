# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42


def check_error(input_data):
    if ' ' in input_data:
        raise ValueError('пробелы недопустимы)')
    elif not input_data.isdigit():
        raise ValueError('Работаем только с цифрами')
    elif len(input_data) < 5:
        raise IndexError('Строка должна содержать пять и более цифр!')


while True:
    try:
        input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
        if not check_error(input_data):
            leeloo = int(input_data[4])
            result = BRUCE_WILLIS * leeloo
            print(f"- Leeloo Dallas! Multi-pass № {result}!")
            break
    except IndexError as exp:
        print(f'{exp}')
    except ValueError as exp:
        print(f'{exp}')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
