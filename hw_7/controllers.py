from models import format_data, get_book_data, export_data
from views import console_view


def export_data_to_book(data: list) -> None:
    """Функция для экспорта данных в телефонную книгу.

    Args:
        data (list): Данные для экспорта
    """
    data_csv = format_data(data)
    data_txt = format_data(data, 'txt')

    export_data(data_csv)
    export_data(data_txt, 'phone_book.txt')


def wipe_book_data() -> None:
    """Функция для полной очистки данных в телефонной книге.
    """
    export_data('', open_mode='w')
    export_data('', 'phone_book.txt', open_mode='w')


def validate_user_input(user_choice: str,
                        valid_choices: list,
                        msg: str = 'Ваш выбор: ') -> str:
    """Функция для проверки правильности введенных пользователем данных.

    Args:
        user_choice (str): Изначальный ввод пользователя
        valid_choices (str): Правильные варианты выбора
        msg (str): Сообщение для отображения при неправильном вводе
    """
    while user_choice not in valid_choices:
        print('Введите правильный вариант!')
        user_choice = input(msg)

    return user_choice


def user_interface() -> None:
    """Функция для отображения пользовательского интерфейса.
    """
    main_menu = [
        'Доступные действия',
        '1. Добавить новый контакт',
        '2. Показать список контактов',
        '3. Стереть данные телефонной книги',
        'Ваш выбор: '
        ]

    export_fields = [
        'фамилию',
        'имя',
        'номер телефона',
        'описание',
    ]

    view_menu = [
        'Выберите формат отображения',
        '1. Имя, Фамилия, Номер телефона, Описание',
        '2. Имя\n   Фамилия\n   Номер телефона\n   Описание\n   ----------',
        'Ваш выбор: '
    ]

    console_view(main_menu, end='')

    user_choice = input()
    user_choice = validate_user_input(user_choice, ['1', '2', '3'])

    if user_choice == '1':
        new_data = []

        for i in range(len(export_fields)):
            field = input(f'Введите {export_fields[i]}: ')
            new_data.append(field)

        export_data_to_book(new_data)

    elif user_choice == '2':
        console_view(view_menu, end='')

        user_choice = input()
        user_choice = validate_user_input(user_choice, ['1', '2'])

        phonebook = get_book_data()
        
        if user_choice == '1':
            if type(phonebook) == list:
                phonebook = [', '.join(el) for el in phonebook]

        elif user_choice == '2':
            fields = export_fields[:]
            fields[0] = 'фамилия'
            
            if type(phonebook) == list:
                delimiter = '-' * 15

                print(delimiter)

                phonebook = [[f'{fields[i].capitalize()}: {el[i]}'
                              for i in range(len(el))]
                            for el in phonebook]

                phonebook = ['\n'.join(el) for el in phonebook]

                for i in range(1, len(phonebook) * 2 , 2): 
                    phonebook.insert(i, delimiter)

        console_view(phonebook)

    elif user_choice == '3':
        user_choice = input('Вы уверены? [y|<other>]: ')

        if user_choice == 'y':
            wipe_book_data()


if __name__ == '__main__':
    user_interface()