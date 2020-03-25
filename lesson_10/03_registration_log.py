# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

FILE_IN = 'registrations.txt'
FILE_GOOD = 'registrations_good.log'
FILE_BAD = 'registrations_bad.log'


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class CheckData:

    def __init__(self, file_in, file_out_right, file_out_wrong):
        self.file_in = file_in
        self.file_out_right = file_out_right
        self.file_out_wrong = file_out_wrong

    def get_files(self):
        with open(self.file_in, 'r') as f:
            for line in f:
                line = line[:-1]
                try:
                    self.check_errors(line)
                except ValueError as exp:
                    self.get_sort_data_file(line, error=exp, file_out=self.file_out_wrong)
                except NotNameError as exp:
                    self.get_sort_data_file(line, error=exp, file_out=self.file_out_wrong)
                except NotEmailError as exp:
                    self.get_sort_data_file(line, error=exp, file_out=self.file_out_wrong)
                else:
                    self.get_sort_data_file(line, error=None, file_out=self.file_out_right)

    def check_errors(self, line):
        fields = list(line.split(' '))
        if len(fields) < 3 or fields is []:
            raise ValueError('Заполненны не все поля')
        if not fields[0].isalpha():
            raise NotNameError('Поле Имя содержит не только буквы')
        if '@' not in fields[1] or '.' not in fields[1]:
            raise NotEmailError('Поле Мейл заполнено не корректно')
        if 10 < int(fields[2]) > 99:
            raise ValueError('Поле Возраст заполнено не корректно')

    def get_sort_data_file(self, line, file_out, error=None):
        with open(file=file_out, mode='a', encoding='utf8') as file:
            if error:
                file.write('{} - {}'.format(line, error))
            else:
                file.write('{}'.format(line))
            file.write('\n')


get_data = CheckData(FILE_IN, FILE_GOOD, FILE_BAD)
get_data.get_files()
