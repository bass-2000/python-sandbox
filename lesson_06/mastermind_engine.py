from random import randint

_holder = []


def make_a_number():
    global _holder
    _holder.append(str(randint(1000, 9999)))


def check_number():
    number = str(input('Попробуйте отгадать число: '))
    print('Вы ввели: ', number)

    list_without_bull = []
    number_without_bull = []

    bull_cow = {'bulls': 0, 'cows': 0}

    for i in range(len(_holder[0])):
        if str(_holder[0][i]) == str(number[i]):
            bull_cow['bulls'] += 1
        else:
            list_without_bull.append(_holder[0][i])
            number_without_bull.append(number[i])

    for i in list_without_bull:
        if i in number_without_bull:
            bull_cow['cows'] += 1
            number_without_bull.remove(i)
    if bull_cow['bulls'] == 4:
        print(bull_cow)
        return True
    print(bull_cow)
    return False
