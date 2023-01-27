from os.path import exists, join
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DISCIPLINES_DIR = join(BASE_DIR, 'disciplines')


def get_disciplines_dict() -> dict:
    with open(join(BASE_DIR, 'all_disciplines.txt'),
              mode='r',
              encoding='utf-8') as f:
        disciplines = f.readlines()

    disciplines = [el.strip('\n').split('=') for el in disciplines]

    disciplines_dict = {el[0]: el[1] for el in disciplines}

    return disciplines_dict


def get_students_dict(discipline: str) -> dict:
    disc_path = join(DISCIPLINES_DIR, discipline + '.txt')

    if exists(disc_path):
        with open(disc_path, 'r', encoding='utf-8') as f:
            stud_list = f.readlines()

        if stud_list:
            stud_list = [el.strip('\n').split() for el in stud_list]

            stud_dict = {el[0]: el[1:] for el in stud_list}

        else:
            stud_dict = {}

    else:
        write_data(disc_path)

        stud_dict = {}

    return stud_dict


def write_data(file_path,
               data: str | list | dict | None = None,
               mode: str = 'w') -> None:
    if type(data) == dict:
        data_lst = [f'{key} {" ".join(value)}'
                    for key, value in data.items()]

        write_data(file_path, data_lst)

    elif type(data) == list:
        data_str = '\n'.join(data)
        write_data(file_path, data_str)

    elif type(data) == str:
        with open(file_path, mode, encoding='utf-8') as f:
            f.write(data + '\n')


if __name__ == "__main__":
    print(get_disciplines_dict())
    print(get_students_dict('russian'))

