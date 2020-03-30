import re


def get_score(game_result):
    wrong_chs = [ch for ch in game_result if ch not in '123456789X/-']
    if wrong_chs:
        raise ValueError("Переданы запрещенные символы: {}".format(''.join(wrong_chs)))

    x_count = game_result.count('X')
    total_score = x_count * 20

    game_result = re.sub(r'[X]', '', game_result)

    game_score_without_x = []
    for x in range(0, len(game_result), 2):
        if len(game_result[x:x + 2]) == 2:
            game_score_without_x.append(game_result[x:x + 2])
        else:
            raise ValueError('Ошибка в фрейме, передан только один результат игры: {}'.format(game_result[x]))

    if x_count + len(game_score_without_x) != 10:
        raise ValueError('Игра должна состоять из десяти фреймов, передано: {}'.
                         format(x_count + len(game_score_without_x)))
    for score in game_score_without_x:
        if re.findall('\d/', score):
            total_score += 15

        elif re.findall('\d-', score) or re.findall('-\d', score):
            total_score += int(re.findall('\d', score)[0])

        elif score == '--':
            total_score += 0

        elif re.findall('\d+', score):
            if '/' in score:
                raise ValueError('Неверные позиции у данных: {}'.format(score))

            numbs = [int(d) for d in score]
            if sum(numbs) > 9:
                raise ValueError('Введено невозможное количество очков: {}, сумма очков не '
                                 'должна привышать 9 баллов'.format(' '.join([d for d in score])))
            total_score += sum(numbs)

        elif score == '//':
            raise ValueError('Некорректная передача данных: {}'.format(score))

    return total_score
