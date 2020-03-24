# -*- coding: utf-8 -*-

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os
import shutil
import time
import zipfile


class Sorting:

    def __init__(self, file_name, new_file_name):
        self.file_name = file_name
        self.new_file_name = new_file_name

    def get_new_file(self):
        for dirpath, dirnames, filenames in os.walk(self.file_name):
            dirs = dirpath.split('/')
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                if os.path.isfile(full_file_path):
                    stat_info_file = os.stat(full_file_path)
                    file_secs = stat_info_file.st_birthtime
                    file_date = time.gmtime(file_secs)
                    new_path = '{}/{}/{}/'.format(self.new_file_name, file_date[0], file_date[1]) + '{}/'.format(
                        dirs[1])
                    self.copy_file(full_file_path, new_path)

    def copy_file(self, old_path, new_path):
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        shutil.copy2(src=old_path, dst=new_path)


class ZipSorting(Sorting):

    def get_new_file(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            dirs = filename.split('/')
            info_file = zfile.getinfo(filename)  # здесь мы получили информацию о файле
            """Достать все Файлы и дату их создания"""
            if not info_file.is_dir():
                """Получить имена директорий"""
                file_date = info_file.date_time  # здесь мы узнали дату (выводится в виде кортежа)
                new_path = '{}/{}/{}/'.format(self.new_file_name, file_date[0], file_date[1]) + '{}/'.format(
                    dirs[1])
                self.copy_file(self.file_name, new_path)


g = ZipSorting('icons.zip', 'newicons_zip')
g.get_new_file()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
