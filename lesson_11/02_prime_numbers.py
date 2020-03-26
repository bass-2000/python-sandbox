# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        """Если число не делится на предшественников с остатком ноль - простое число, его добавляют в prime numb
        если нет оно порпускает, берется след."""
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, number):  # n=10, предел
        self.current_number = 1  # текущее число
        self.prime_numbers = []  # список простых чисел
        self.max_number = number  # максимальное число

    def __iter__(self):
        return self

    def get_prime(self):
        for prime in self.prime_numbers:
            if self.current_number % prime == 0:
                return False
        else:
            return True

    def __next__(self):
        self.current_number += 1
        if self.current_number <= self.max_number:
            while not self.get_prime():
                if self.current_number < self.max_number:
                    self.current_number += 1
                else:
                    raise StopIteration()
            else:
                self.prime_numbers.append(self.current_number)
                return self.current_number


# prime_number_iterator = PrimeNumbers(number=10000)
# for number in prime_number_iterator:
#     print(number)
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def true_happy_number(number):
    number = list(map(int, (str(number))))
    middle_number = len(number) // 2
    left_part = sum(number[:middle_number])
    right_part = sum(number[-middle_number:])
    return left_part == right_part and len(number) > 1


def true_reverse_number(number):
    number = str(number)
    reverse_number = ''.join(reversed(number))
    return number == reverse_number and len(number) > 1


def true_repdigit_number(number):
    number_check = set(str(number))
    return len(number_check) == 1 and len(str(number)) > 1


def get_prime(current_number, numbers):
    for prime in numbers:
        if current_number % prime == 0:
            return False
    else:
        return True


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        if get_prime(current_number=number, numbers=prime_numbers):
            prime_numbers.append(number)
            if true_repdigit_number(number):
                yield f'repdigit number {number}'
            elif true_reverse_number(number):
                yield f'reverse number {number}'
            elif true_happy_number(number):
                yield f'happy number {number}'
            else:
                yield f'just prime number {number}'


# for number in prime_numbers_generator(n=10):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def true_happy_number(func):
    def decorator_1(max_number):
        for number in func(max_number):
            check_number = list(map(int, (str(number))))
            middle_number = len(check_number) // 2
            left_part = sum(check_number[:middle_number])
            right_part = sum(check_number[-middle_number:])
            if left_part == right_part and len(check_number) > 1:
                yield f'{number} простое число счастья!'
            else:
                continue

    return decorator_1


def true_reverse_number(func):
    def decorator_2(max_number):
        for number in func(max_number):
            number = str(number)
            reverse_number = ''.join(reversed(number))
            if number == reverse_number and len(number) > 1:
                yield f'{number}  простое палиндромное число!'
            else:
                continue

    return decorator_2


def true_repdigit_number(func):
    def decorator_3(max_number):
        for number in func(max_number):
            number_check = set(str(number))
            if len(number_check) == 1 and len(str(number)) > 1:
                yield f'{number} это простое число состоит из повторяющихся цифр!'
            else:
                continue

    return decorator_3


def get_prime(current_number, numbers):
    for prime in numbers:
        if current_number % prime == 0:
            return False
    else:
        return True


@true_happy_number
# @true_reverse_number
# @true_repdigit_number
def prime_numbers_generator(max_number):
    prime_numbers = []
    for number in range(2, max_number + 1):
        if get_prime(current_number=number, numbers=prime_numbers):
            prime_numbers.append(number)
            yield number


for number in prime_numbers_generator(max_number=5555):
    print(number)
