#* Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет Победитель - тот, кто оставил на столе 0 конфет.
# a) Добавьте игру против бота
# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

from random import randint


def smart_bot_move(candies_cnt: int, max_candies: int, player_candies: int) -> int:
    """Функция для вычисления нужного количества конфет.
    Умнее не придумал) Бота можно обыграть, если оставить ему 29 конфет.

    Args:
        candies_cnt (int): Общее кол-во конфет на данный момент
        max_candies (int): Максимальное кол-во конфет, которое можно взять за ход
        player_candies (int): Кол-во конфет, которое брал человек
    """
    if candies_cnt - max_candies < 1:
        return max_candies + (candies_cnt - max_candies)

    if candies_cnt - player_candies > max_candies:
        return player_candies

    if candies_cnt <= max_candies * 2:
        res_value = candies_cnt - (max_candies + 1)
        return res_value if res_value else max_candies

    return max_candies



def restart_game(candies_cnt: int) -> tuple[int, str]:
    """Функция для принятия решения о перезапуске игры.

    Args:
        candies_cnt (int): Начальное количество конфет в новой игре
    """
    
    decision = input('Для продолжения нажмите ENTER. Для завершения напишите что-нибудь: ')

    if decision:
        return 0, 'Спасибо за игру!'

    return candies_cnt, 'Перезапуск игры...'


def check_candies(candies_cnt: int, took_candies: int, max_candies: int) -> bool:
    """Функция для проверки валидности количества конфет.

        Args:
            candies_cnt (int): Общее кол-во конфет на данный момент
            took_candies (int): Кол-во конфет, которое хочет взять человек
            max_candies (int): Максимальное кол-во конфет, которое можно взять за ход
    """
    if (took_candies > max_candies) or (took_candies < 1):
        print(f'Конфеты можно брать только в диапазоне [1-{max_candies}]!')
        return False

    if took_candies > candies_cnt:
        print('На столе осталось меньше конфет!')
        return False

    return True


def move(candies_cnt: int, is_bot: bool = False, max_candies: int = 28, took_candies: int = 0) -> int:
    """Функция для выполнения хода человеком/ботом.

        Args:
            candies_cnt (int): Общее кол-во конфет на данный момент
            is_bot (bool): False Флаг для определения хода человека/бота
            max_candies (int): 28 Максимальное кол-во конфет, которое можно взять за ход
            took_candies (int): 0 Кол-во конфет, которое брал человек (нужно для 'умного' бота)
    """
    candies_limit = max_candies if candies_cnt >= max_candies else candies_cnt

    if not is_bot:
        is_candies_valid = False

        while not is_candies_valid:
            took_candies = int(input(f'Введите количество конфет (1-{candies_limit}): '))
            is_candies_valid = check_candies(candies_cnt, took_candies, candies_limit)
        
        return took_candies

    #!!!!!!!!!! a) Глупый бот)
    # took_candies = randint(1, candies_limit)

    #!!!!!!!!!! b) Умный бот)
    took_candies = smart_bot_move(candies_cnt, max_candies, took_candies)

    return took_candies


def init_game(candies: int = 120) -> None:
    """Фунция для первоначальной инициализации игры.

        Args:
            candies: int (default: 20) Количество конфет, с которого начинается игра
    """
    candies_cnt = candies

    print(f'На столе {candies} конфет')

    while candies_cnt:

        took_candies = move(candies_cnt)
        candies_cnt -= took_candies

        print(f'Вы взяли {took_candies} конфет, осталось {candies_cnt}')

        if not candies_cnt:
            print('Вы выиграли!')

            candies_cnt, msg = restart_game(candies)

            print(msg)

            continue

        took_candies = move(candies_cnt, is_bot=True, took_candies=took_candies)
        candies_cnt -= took_candies

        print(f'Бот взял {took_candies} конфет, осталось {candies_cnt}')
        
        if not candies_cnt:
            print('Выиграл бот!')

            candies_cnt, msg = restart_game(candies)

            print(msg)

            continue


if __name__ == '__main__':
    init_game()
