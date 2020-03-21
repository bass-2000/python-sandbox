# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
exp = 2000

month, result = 0, 0
how_many = 0
while month < 10:
    educational_grant += 10000
    print(f'edu = {educational_grant}')
    if month > 1:
        expenses += 12000 + (expenses / 100 * 3)
        print(f'exp = {expenses}')
    else:
        expenses += 12000
    result = expenses - educational_grant
    how_many += result
    month += 1
    print(f'res = {result}')
