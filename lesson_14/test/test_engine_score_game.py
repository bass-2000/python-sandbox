import unittest

from ..bowling.engine_score_game import get_score


class GetScoreTest(unittest.TestCase):

    def test_normal(self):
        result = get_score('X23---12-22X134---')
        self.assertEqual(result, 60)

    def test_dashes(self):
        result = get_score('--------------------')
        self.assertEqual(result, 0)

    def test_null(self):
        with self.assertRaisesRegex(ValueError, 'Игра должна состоять из десяти фреймов, передано: 0'):
            get_score(game_result='')

    def test_raise_value_exc(self):
        with self.assertRaisesRegex(ValueError, 'Игра должна состоять из десяти фреймов, передано: 9'):
            get_score('X23---12-22X134-')

    def test_reversed_value_exc(self):
        with self.assertRaisesRegex(ValueError, 'Переданы запрещенные символы: 0'):
            get_score('X23---12-22X134--0')

    def test_wrong_value_exc(self):
        with self.assertRaisesRegex(ValueError, 'Введено невозможное количество очков: 9 8, сумма очков не '
                                                'должна привышать 9 баллов'):
            get_score('XXX983-X2-2176--')

    def test_wrong_position_value(self):
        with self.assertRaisesRegex(ValueError, 'Неверные позиции у данных: /1'):
            get_score('X/1XXXXXXXX')

    def test_wrong_send_data(self):
        with self.assertRaisesRegex(ValueError, 'Некорректная передача данных: //'):
            get_score('//XXXXXXXXX')

        def test_wrong_count_score(self):
            with self.assertRaisesRegex(ValueError, 'Ошибка в фрейме, передан только один результат игры: 7'):
                get_score('--4/XXX7XXXXX')


if __name__ == '__main__':
    unittest.main()
