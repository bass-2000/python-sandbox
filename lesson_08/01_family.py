# -*- coding: utf-8 -*-

from random import randint, choice

import numpy
from termcolor import cprint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    total_take_food = 0
    residents = []

    def __init__(self):
        self.money_in_the_nightstand = 100
        self.food_in_fridge = 50
        self.capacity_fridge = 100
        self.dirty = 0
        self.cat_food = 30
        self.residents = []
        self.pets = []


class Human:
    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house
        self.house.residents.append(self)

    def __str__(self):
        return 'Я {}, моя сытость: {}, мой уровень счастья: {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        take_food = 0
        if self.house.food_in_fridge < 10:
            self.fullness -= 5
            # cprint('В доме нет еды')
            return True
        else:
            if self.house.food_in_fridge >= 30:
                take_food = randint(10, 30)
            elif 10 <= self.house.food_in_fridge < 30:
                take_food = randint(10, self.house.food_in_fridge)
            self.fullness += take_food
            self.house.food_in_fridge -= take_food
            self.house.total_take_food += take_food
            cprint('{} покушал. Еды съедено {}'.format(self.name, take_food), color='red')
            return False

    def pet_cat(self):
        self.happiness += 5
        cprint('{} погладил кота'.format(self.name), color='green')

    def act(self):
        if self.fullness < 0 or self.happiness < 10:
            cprint('{} скоропостижно скончался'.format(self.name), color='red')
            self.house.residents.remove(self)
            return False
        elif self.fullness <= 15:
            if self.eat():
                return True
            else:
                return False

        else:
            return True


class Husband(Human):
    money_earned = 0

    def __init__(self, name, house, salary):
        super().__init__(name, house)
        self.salary = salary

    def act(self):
        if super().act() is True:
            dice = randint(1, 6)
            if self.house.money_in_the_nightstand < 150:
                self.work()
            elif self.happiness <= 15:
                self.gaming()
            elif self.house.cat_food <= 15:
                self.buy_cat_food()
            elif dice == 1:
                self.work()
            elif dice == 2:
                self.pet_cat()
            elif dice == 3:
                self.eat()
            else:
                self.gaming()

    def work(self):
        self.house.money_in_the_nightstand += 150
        self.fullness -= 10
        self.money_earned += 150
        cprint('{} сходил на работу'.format(self.name), color='blue')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        cprint('{} поиграл в WoT'.format(self.name), color='green')

    def buy_cat_food(self):
        if self.house.money_in_the_nightstand >= 30:
            cprint('{} Купил корм для своего кота'.format(self.name), color='grey')
            self.house.cat_food += 20 * len(self.house.pets)
            self.house.money_in_the_nightstand -= 20 * len(self.house.pets)


class Wife(Human):
    fur_coat = 0

    def act(self):
        if super().act() is True:
            dice = randint(1, 6)
            if self.house.food_in_fridge <= 80:
                self.shopping()
            elif self.house.dirty >= 90:
                self.clean_house()
            elif self.happiness <= 15:
                self.buy_fur_coat()
            elif dice == 1:
                self.shopping()
            elif dice == 2:
                self.buy_fur_coat()
            elif dice == 3:
                self.clean_house()
            elif dice == 4:
                self.pet_cat()
            else:
                self.watch_TV()

    def shopping(self):
        if self.house.money_in_the_nightstand >= 80:
            self.house.food_in_fridge += 80
            self.house.money_in_the_nightstand -= 80
        self.fullness -= 10

    def buy_fur_coat(self):
        if self.house.money_in_the_nightstand > 350:
            self.house.money_in_the_nightstand -= 350
            self.happiness += 60
            self.fur_coat += 1
        self.fullness -= 10

    def clean_house(self):
        if self.house.dirty <= 0:
            return
            cprint('Дом чист!')
        else:
            self.house.dirty -= randint(10, 100)
            self.fullness -= 10
            cprint('{} прибралась'.format(self.name), color='white')

    def watch_TV(self):
        self.happiness += 10
        self.fullness -= 10


class Child(Human):

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food_in_fridge >= 10:
            take_food = randint(5, 10)
            self.fullness += take_food
            self.house.total_take_food += take_food

    def sleep(self):
        self.fullness -= 10


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30
        self.house.residents.append(self)
        self.house.pets.append(self)

    def __str__(self):
        return 'Это {}, он сыт на: {}'.format(self.name, self.fullness)

    def act(self):
        if self.fullness < 0:
            cprint('{} помер'.format(self.name))
            self.house.residents.remove(self)
            return
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.soil()

    def eat(self):
        if self.house.cat_food <= 0:
            return
            cprint('{} не может найти еду дома!'.format(self.name), color='green')
        else:
            get_cat_food = randint(2, 10)
            self.fullness += get_cat_food * 2
            self.house.cat_food -= get_cat_food
            cprint('{} поел'.format(self.name), color='green')

    def sleep(self):
        self.fullness -= 10
        cprint('{} поспал'.format(self.name), color='green')

    def soil(self):
        self.fullness -= 10
        self.house.dirty += 5
        cprint('{} дерет обои'.format(self.name), color='green')


class Fail:
    days_money_incidents = []
    days_food_incidents = []

    def __init__(self, n_food_incidents, n_money_incidents, house):
        self.days_food_incidents = numpy.random.randint(1, 365, n_food_incidents)
        self.days_money_incidents = numpy.random.randint(1, 365, n_money_incidents)
        self.house = house

    def fail_happened(self, day):
        if day in self.days_money_incidents:
            self.house.money_in_the_nightstand //= 2
        else:
            return
        if day in self.days_food_incidents:
            self.house.food_in_fridge //= 2
        else:
            return


def life_simulation():
    cat_names_keys = list(cat_names.keys())
    home = House()
    Husband(name='Сережа', house=home, salary=salary)
    Wife(name='Маша', house=home)
    Child(name='Коля', house=home)
    for day in range(366):
        if len(home.pets) * 10 <= home.cat_food and len(home.pets) * 20 <= home.money_in_the_nightstand and home.dirty \
                <= 10:
            if not cat_names_keys:
                print('Я бы взял кота, но фантазия на имена кончилась')
            else:
                cat_name = choice(cat_names_keys)
                cat_names_keys.remove(cat_name)
                cat = Cat(name=cat_names[cat_name], house=home)
                cprint('В доме завелся кот! Назвали {}'.format(cat.name), color='green')
        home.dirty += 5
        for resident in home.residents:
            resident.act()
            if home.dirty > 90 and resident is Human and resident is not Child:
                resident.happiness -= 10
        for resident in home.residents:
            cprint(resident, color='cyan')
        cprint(home, color='cyan')


def live_experiment(date_fail_food, date_fail_money):
    """Вариант реализации задачи через функцию"""
    cat_names_keys = list(cat_names.keys())
    home = House()
    Husband(name='Сережа', house=home, salary=salary)
    Wife(name='Маша', house=home)
    Child(name='Коля', house=home)
    for day in range(366):
        if day in date_fail_food:
            home.food_in_fridge //= 2
        if day in date_fail_money:
            home.money_in_the_nightstand //= 2
        if (len(home.pets) * 10 <= home.cat_food
                and len(home.pets) * 20 <= home.money_in_the_nightstand
                and home.dirty <= 10
        ):
            if not cat_names_keys:
                return
            else:
                cat_name = choice(cat_names_keys)
                cat_names_keys.remove(cat_name)
                Cat(name=cat_names[cat_name], house=home)

        home.dirty += 5
        for resident in home.residents:
            resident.act()
            if home.dirty > 90 and resident is Human and resident is not Child:
                resident.happiness -= 10
    return len(home.pets)


def live_experiment_2(food_fails, money_fails):
    """Вариант реализации задачи через класс"""
    cat_names_keys = list(cat_names.keys())
    home = House()
    Husband(name='Сережа', house=home, salary=salary)
    Wife(name='Маша', house=home)
    Child(name='Коля', house=home)
    dark_days = Fail(n_food_incidents=food_fails, n_money_incidents=money_fails, house=home)
    for day in range(366):
        dark_days.fail_happened(day=day)
        if (len(home.pets) * 10 <= home.cat_food
                and len(home.pets) * 20 <= home.money_in_the_nightstand
                and home.dirty <= 10
        ):
            if not cat_names_keys:
                return
            else:
                cat_name = choice(cat_names_keys)
                cat_names_keys.remove(cat_name)
                Cat(name=cat_names[cat_name], house=home)

        home.dirty += 5
        for resident in home.residents:
            resident.act()
            if home.dirty > 90 and resident is Human and resident is not Child:
                resident.happiness -= 10
    return len(home.pets)


def create_fails(n):
    """Создает список дней, в которые произойдет определенное событие. Количество задается в параметре n"""
    dark_days = []
    for i in range(0, n):
        dark_day = randint(1, 366)
        dark_days.append(dark_day)
    return sorted(dark_days)


cat_names = {
    """Тело программы реализованно на варианте решения через класс"""
    "bedolaga": 'Бедолага',
    'captain_coco': 'Капитан Кокс',
    'admiral_kruzenstern': 'Адмирал Крузенштерн',
    'godfather': 'Крестный Отец',
    'pugovka': 'Пуговка',
    'kukuruzinka': 'Кукурузинка',
    'aleshka': 'Алешка',
    'mishka': 'Мышка',
    'markiza': 'Маркиза',
    'volk': 'Волк',
    'korol': 'Король',
    'kony': 'Конь'
}

final_max_cats = 0
for food_incidents in range(1, 7):
    for money_incidents in range(1, 7):
        total_cats = 0
        for salary in range(50, 401, 150):
            """Проводим эксперимент три раза"""
            max_cats_1 = live_experiment_2(food_fails=food_incidents, money_fails=money_incidents)
            max_cats_2 = live_experiment_2(food_fails=food_incidents, money_fails=money_incidents)
            max_cats_3 = live_experiment_2(food_fails=food_incidents, money_fails=money_incidents)
            """Считаем среднее количество кошек, выживших по результатам этих трех эксп-в"""
            average_cats = (max_cats_1 + max_cats_2 + max_cats_3) // 3
            total_cats += average_cats
            """Рассчитываем максимальное кол-во параметров всех эксп-в"""
            if average_cats > final_max_cats:
                final_max_cats = average_cats
                final_fails = food_incidents + money_incidents

cprint('Максимальное количество котов было {}, при количестве инцидентов {}'.format(final_max_cats,
                                                                                    final_fails), color='green')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
