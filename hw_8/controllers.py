from os.path import exists, join
from pathlib import Path

from db_scripts import (BASE_DIR,
                        DISCIPLINES_DIR,
                        get_disciplines_dict,
                        get_students_dict,
                        write_data)
from search import search_discipline, search_student
# from utils import transliteration

# Отключил специально, так слишком много делать еще)

# def add_discipline(discipline_name: str):
#     discipline_translit = transliteration(discipline_name)
#     write_data(join(BASE_DIR, 'all_disciplines.txt'),
#                f'{discipline_name}={discipline_translit}',
#                'a')
#     write_data(join(DISCIPLINES_DIR, f'{discipline_translit}.txt'))

# В интерфейсе даже не стал прописывать дополнительный пункт


def add_student(discipline: str, student_name: str, grade: str):
    write_data(join(DISCIPLINES_DIR, f'{discipline}.txt'),
               f'{student_name} {grade}',
               'a')


def add_grade(discipline: str, student_name: str, grade: str):
    stud_dict = get_students_dict(discipline)

    stud_dict[student_name].append(grade)

    write_data(join(DISCIPLINES_DIR, f'{discipline}.txt'), stud_dict)


def user_interface():
    print('Выберите роль:\n1. Преподаватель\n2. Ученик\n')

    decision = input('Ваша роль: ')

    if decision == '1':
        print('\nСписок предметов:')
        print('\n'.join(get_disciplines_dict().keys()) + '\n')

        discipline = input('Введите название предмета: ')

        search_res = search_discipline(discipline)

        if search_res[0]:
            student = input('Введите фамилию ученика: ').capitalize()

            if not search_student(search_res[1], student):
                grade = input('Введите оценку: ')

                add_student(search_res[1], student, grade)

            else:
                grade = input('Введите оценку: ')

                add_grade(search_res[1], student, grade)

        else:
            print('Такого предмета нет в списке!')

    elif decision == '2':
        surname = input('Введите вашу фамилию: ')

        for name, filename in get_disciplines_dict().items():
            if search_student(filename, surname):
                print(f'{name}: {", ".join(get_students_dict(filename)[surname])}')


if __name__ == "__main__":
    user_interface()
