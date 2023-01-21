def console_view(data: list | str, end: str = '\n') -> None:
    """Функция для данных в консоли.

    Args:
        data (list | str): Данные для отображения
        end (str): "\\n" Строка, добавляемая после основного вывода
    """
    if type(data) == list:
        data_cp = data[:]
        data_cp = '\n'.join(data_cp)

        print(data_cp, end=end)

    elif type(data) == str:
        print(data + end)