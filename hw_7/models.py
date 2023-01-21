from os.path import exists, join
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def get_book_data(file_path: str = 'phone_book.csv') -> list | str:
    """Функция для получения данных из файла телефонной книги.

    Args:
        file_path (str): phone_book.csv Путь к файлу телефонной книги
    """
    if exists(join(BASE_DIR, file_path)):
        with open(join(BASE_DIR, file_path), 'r', encoding='utf-8') as f:
            book_data = f.readlines()

        for i in range(len(book_data)):
            book_data[i] = book_data[i].strip('\n')
            book_data[i] = book_data[i].split(', ')

        return book_data

    return 'В телефонной книге нет записей!'


def export_data(data: str,
                file_path: str = 'phone_book.csv',
                open_mode: str = 'a') -> None:
    """Функция для записи данных в файл телефонной книги.

    Args:
        data (str): Данные для записи
        file_path (str): phone_book.csv Путь к файлу телефонной книги
        open_mode (str): "a" Режим открытия файла
    """
    with open(join(BASE_DIR, file_path), open_mode, encoding='utf-8') as f:
        f.write(data)


def format_data(data: list,
                file_type: str = 'csv',
                delimiter: str = '-') -> str:
    """Функция для записи данных в файл телефонной книги.

    Args:
        data (str): Данные для записи
        file_type (str): csv Тип файла (csv или txt)
        delimiter (str): "-" Разделитель записей (Только для формата txt!)
    """
    data_fields = ['Фамилия: ', 'Имя: ', 'Номер телефона: ', 'Описание: ']

    if file_type == 'csv':
        formatted_data = ', '.join(data) + '\n'

    elif file_type == 'txt':
        formatted_data = data[:]

        for i in range(len(formatted_data)):
            formatted_data[i] = data_fields[i] + formatted_data[i]

        formatted_data.append(delimiter * 10 + '\n')

        formatted_data = '\n'.join(formatted_data)

    else:
        formatted_data = 'None\n'

    return formatted_data