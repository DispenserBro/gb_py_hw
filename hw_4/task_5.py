import os.path
from pathlib import Path

# ХА, а мне меньше писать теперь надо)
from task_4 import generate_polynom, get_polynom

#* Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов

def get_pows_dict(lst_in: list) -> dict:
    pows_dict = {}
    
    for el in lst_in:
        if 'x' not in el:
            if 0 in pows_dict.keys():
                pows_dict[0] += int(el[0])

            else:
                pows_dict[0] = int(el[0])

        else:
            if len(el) == 1:
                if 1 in pows_dict.keys():
                    pows_dict[1] += 1

                else:
                    pows_dict[1] = 1

            elif len(el) == 2:
                if el[0] == 'x':
                    if int(el[1]) in pows_dict.keys():
                        pows_dict[int(el[1])] += 1

                    else:
                        pows_dict[int(el[1])] = 1

                else:
                    if 1 in pows_dict.keys():
                        pows_dict[1] += int(el[0])

                    else:
                        pows_dict[1] = int(el[0])

            else:
                if int(el[2]) in pows_dict.keys():
                    pows_dict[int(el[2])] += int(el[0])

                else:
                    pows_dict[int(el[2])] = int(el[0])

    return pows_dict

def process_polynoms(lst: list) -> str:
    lst_cp = lst[:]

    for el in lst_cp:
        if el == '':
            lst_cp.remove(el)

    for i in range(len(lst_cp)):
        lst_cp[i] = lst_cp[i].replace('^', '*').split('*')

    pows_dict = get_pows_dict(lst_cp)

    result = generate_polynom(pows_dict)

    return ' + '.join(result)

# Неудачный вариант: не получится запускать скрипт отовсюду (например, из корневой папки с дз по python и т.п)
# with open('./polynoms/polynom_1.txt', 'r') as f1:

# Универсальный вариант: работает отовсюду)
# В Django используется Path(__file__).resolve().parent.parent
# т.к Корневой считается папка проекта

BASE_DIR = Path(__file__).resolve().parent
polynoms_folder = os.path.join(BASE_DIR, 'polynoms')

# если хочется рандомных многочленов)

# max_power = int(input('Enter the maximal power of the 1st polynom: '))

# with open(os.path.join(polynoms_folder, 'polynom_1.txt'), 'w') as f1:
#     res1 = get_polynom(max_power)
#     f1.write(res1)

# max_power = int(input('Enter the maximal power of the 2nd polynom: '))

# with open(os.path.join(polynoms_folder, 'polynom_2.txt'), 'w') as f2:
#     res2 = get_polynom(max_power)
#     f2.write(res2)

lst_in = []

with open(os.path.join(polynoms_folder, 'polynom_1.txt'), 'r') as f1:
    # Тут все по условным данным, иначе сложнее было бы(
    res1 = f1.read()
    lst_in = res1.split(' + ')

with open(os.path.join(polynoms_folder, 'polynom_2.txt'), 'r') as f2:
    res2 = f2.read()
    lst_in += res2.split(' + ')

with open(os.path.join(polynoms_folder, 'polynom_res.txt'), 'w') as res:
    res.write(process_polynoms(lst_in))


# Посмотреть, что было и что стало)

# print(res1)
# print(res2)
# print(process_polynoms(lst_in))
