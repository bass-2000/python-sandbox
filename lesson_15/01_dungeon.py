# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход


import csv
import json
import re
import sys
from datetime import timedelta
from decimal import Decimal


class DungeonRPG:

    def __init__(self, file):
        self.file = file
        self.remaining_time = '1234567890.0987654321'
        self.current_experience = 0
        self.current_date = 0
        self.location_name = ''
        self.list_monsters = []
        self.list_locations = []
        self.map = {}
        self.key = True

    def load_file(self):
        with open(self.file, 'r') as read_file:
            self.map = json.load(read_file)

    def parse_location(self):
        """
        Заполнение списков монстров и переходов в текущей локации.
        :return: None
        """
        for loc in self.map.keys():
            self.location_name = loc
            for val in self.map[loc]:
                if type(val) == dict:
                    for key in val.keys():
                        self.list_locations.append(key)
                elif type(val) == list:
                    for n in val:
                        self.list_monsters.append(n)
                else:
                    self.list_monsters.append(val)

    def time_count(self, time_object):
        """
        Подсчет оставшегося времени (remaining_time) и текущего (current_date)
        :param time_object: строка с вхождением *tm
        :return: None
        """
        time_elapsed = Decimal(re.search(r'tm\d+', time_object)[0][2:])
        self.remaining_time = Decimal(self.remaining_time) - time_elapsed
        self.current_date += time_elapsed

    def monster_count(self, monster_name):
        """
        Подсчет полученного опыта (current_experience) за убийство монстра и учет времени боя с ним.
        :param monster_name: строка названия монстра
        :return: None
        """
        exp_received = int(re.search(r'exp\d+', monster_name)[0][3:])
        self.current_experience += exp_received
        self.time_count(monster_name)
        print(f'Получено опыта - {exp_received}, всего - {self.current_experience}')

    def monster_attack(self):
        """
        Обработка события выбора монстра
        :return: None
        """
        if len(self.list_monsters) > 1:
            for i in range(len(self.list_monsters)):
                print(f'{i + 1} - Атаковать монстра {self.list_monsters[i]}')
            print('Выберити монстра, чтобы атаковать:')
            choice = int(input('> '))
        else:
            choice = 1
        monster_killed = self.list_monsters.pop(choice - 1)
        print(f'Монстр {monster_killed} повержен!')
        self.monster_count(monster_killed)
        self.key = False

    def choose_action(self):
        """
        Выбор действия в соответствии с присутствием в локации монстров либо перехода в другую локацию.
        :return: None
        """
        if len(self.list_locations) > 0 or len(self.list_monsters) > 0:
            print(f'Выберите действие: ')
        if len(self.list_locations) == 0:
            if len(self.list_monsters) == 0:
                print('Поздравляем вы прошли подземелье!')
                sys.exit()
            print(f'1.Атаковать монстра')
            print(f'2.Выход')
            print('>>> Это последняя комната! <<<')
            while True:
                action = int(input('> '))
                if action == 1:
                    self.monster_attack()
                    return
                elif action == 2:
                    sys.exit()
                else:
                    print('Введите 1 или 2!')
        elif len(self.list_monsters) == 0:
            print(f'1.Перейти в другую локацию')
            print(f'2.Выход')
            while True:
                action = int(input('> '))
                if action == 1:
                    self.change_location()
                    return
                elif action == 2:
                    sys.exit()
                else:
                    print('Введите 1 или 2!')

        else:
            print(f'1.Атаковать монстра')
            print(f'2.Перейти в другую локацию')
            print(f'3.Выход')
            while True:
                action = int(input('> '))
                if action == 1:
                    self.monster_attack()
                    return
                elif action == 2:
                    self.change_location()
                    return
                elif action == 3:
                    sys.exit()
                else:
                    print('Введите 1, 2 или 3!')

    def change_location(self):
        """
        Обработка действия выбора локации для перехода и сам переход со сменой текущих значений локации.
        :return: None
        """
        if len(self.list_locations) > 1:
            for i in range(len(self.list_locations)):
                print(f'{i + 1} - Перейти в локацию {self.list_locations[i]}')
            print('Выберити локацию для перехода:')
            choice = int(input('> '))
        else:
            choice = 1
        next_location = self.list_locations[choice - 1]
        for pos in self.map[self.location_name]:
            if type(pos) == dict:
                if pos.get(next_location):
                    self.map = pos
        self.key = True
        self.location_name = next_location
        self.time_count(self.location_name)
        self.list_locations = []
        self.list_monsters = []

    def run(self):
        """
        Цикл прохождения локаций и запись данных в csv.
        :return: None
        """
        with open('dungeon.csv', 'w', newline='') as out_csv:
            writer = csv.writer(out_csv)
            line = ['current_location', 'current_experience', 'current_date']
            writer.writerow(line)
            while True:
                if self.key:
                    self.parse_location()
                if len(self.list_locations) > 0 or len(self.list_monsters) > 0:
                    print(f'Вы находитесь в {self.location_name}')
                    print(f'У вас {self.current_experience} опыта и осталось {self.remaining_time} секунд')
                    print(f'Прошло уже: {timedelta(seconds=int(self.current_date))}')
                    print(f'Внутри вы видите:')
                for loc in self.list_monsters:
                    print(f'-- Монстра: {loc}')
                for loc in self.list_locations:
                    print(f'-- Вход в локацию: {loc}')
                line = [self.location_name, self.current_experience, timedelta(seconds=int(self.current_date))]
                writer.writerow(line)
                self.choose_action()
                print('*' * 50)


if __name__ == '__main__':
    rpg = DungeonRPG('rpg.json')
    rpg.load_file()
    rpg.run()

# Учитывая время и опыт, не забывайте о точности вычислений!
