# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

import zipfile

FILE_IN = 'events.txt'


class IterTreatmentLog:

    def __init__(self, file_in):
        self.file_in = file_in
        self.selected_NOK_lines = {}
        self.get_stat()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.index <= len(self.selected_NOK_lines):
            return list(self.selected_NOK_lines.items())[self.index - 1]
        else:
            raise StopIteration()

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_in, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_in = filename

    def get_stat(self):
        if self.file_in.endswith('.zip'):
            self.unzip()
        with open(file=self.file_in, mode='r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    new_line = line[:17] + ']'
                    if new_line in self.selected_NOK_lines:
                        self.selected_NOK_lines[new_line] += 1
                    else:
                        self.selected_NOK_lines[new_line] = 1


######################################################################################################################


class GenerateTreatmentLog:

    def __init__(self, name_file_in):
        self.file_in = name_file_in
        self.selected_NOK_lines = {}

    def get_result(self):
        self.get_stat()
        for key, value in self.selected_NOK_lines.items():
            yield key, value

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_in, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_in = filename

    def get_stat(self):
        if self.file_in.endswith('.zip'):
            self.unzip()
        with open(file=self.file_in, mode='r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    new_line = line[:17] + ']'
                    if new_line in self.selected_NOK_lines:
                        self.selected_NOK_lines[new_line] += 1
                    else:
                        self.selected_NOK_lines[new_line] = 1


grouped_events = IterTreatmentLog(FILE_IN)
for group_time, event_count in grouped_events:
    print(f'{group_time} {event_count}')

grouped_events = GenerateTreatmentLog(FILE_IN)
for group_time, event_count in grouped_events.get_result():
    print(f'{group_time} {event_count}')
