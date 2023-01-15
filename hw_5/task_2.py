#* Создайте программу для игры в ""Крестики-нолики"" человек vs человек

def print_field(field: list) -> None:
    """Функция для вывода поля в консоль.

        Args:
            field: list Игровое поле
    """
    for el in field:
        el_str = ' ' + ' | '.join(map(str, el)) + ' '

        if el == field[-1]:
            print(el_str)

        else:
            print(el_str)
            print('___________')


def check_cell(pos: int, field: list, is_player: bool = True) -> bool:
    """Функция для проверки доступности клетки.

        Args:
            pos: int Позиция в диапазоне [1-9]
            field: list Игровое поле
    """
    in_row = 3

    if 0 < pos < 10:
        pos_x = [2, 0, 1][pos % in_row]
        pos_y = int(pos > in_row) + int(pos > in_row * 2)

        if field[pos_y][pos_x] == pos:
            return True

    if is_player:
        print('Кленка занята или находится вне диапазона [1-9]')

    return False


def check_win(field: list, character: str) -> bool:
    """Функция для определения выигрыша по позициям.

        Args:
            field: list Игровое поле
            character: str Символ (Х или О) для проверки выигрыша
    """
    win = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
    )

    for positions in win:
        values = [field[position[0]][position[1]] for position in positions]

        if all(el == character for el in values):
                return True

    return False


def restart_game() -> tuple[bool, str]:
    """Функция для принятия решения о перезапуске игры.
    """
    decision = input('Для продолжения нажмите ENTER. Для завершения напишите что-нибудь: ')

    if decision:
        return False, 'Спасибо за игру!'

    return True, 'Перезапуск игры...'


def move(pos: int, charactrer: str, field: list) -> list:
    """Функция для выполнения хода игрока(бота).

        Args:
            pos: int Позиция в диапазоне [1-9]
            character: str Символ для хода(заменяет число а списке)
            field: list Игровое поле
    """
    in_row = 3
    pos_x = [2, 0, 1][pos % in_row]
    pos_y = int(pos > in_row) + int(pos > in_row * 2)

    field[pos_y][pos_x] = charactrer

    print_field(field)
    return field


def new_game() -> tuple[bool, list]:
    """Функция для запуска новой игры.
    """
    run_game = True

    # Очень страшная штука, но работает правильно
    field = [[1 + j + i + ((i % 3)) * 2 for j in range(3) ] for i in range(3)]

    print_field(field)
    return run_game, field


def init_game() -> None:
    """Функция для первоначальной инициализации игры.
    """
    run_game, field = new_game()
    is_cell = False

    # print_field(field)

    while run_game:
        while not is_cell:
            cell = int(input('Ходят крестики.\nВведите номер клетки [1-9]: '))
            is_cell = check_cell(cell, field)

        is_cell = False

        move(cell, 'X', field)

        if check_win(field, 'X'):
            print('Выиграли крестики!!!!')

            run_game, msg = restart_game()

            print(msg)

            if run_game:
                _, field = new_game()

            continue

        if not any(check_cell(cell, field, is_player=False) for cell in range(1,10)):
            print('Ничья!!!!')

            run_game, msg = restart_game()

            print(msg)

            if run_game:
                _, field = new_game()

            continue

        while not is_cell:
            cell = int(input('Ходят нолики.\nВведите номер клетки [1-9]: '))
            is_cell = check_cell(cell, field)

        is_cell = False

        move(cell, 'O', field)

        if check_win(field, 'O'):
            print('Выиграли нолики!!!!')

            run_game, msg = restart_game()

            print(msg)

            if run_game:
                _, field = new_game()

            continue


if __name__ == '__main__':
    init_game()
