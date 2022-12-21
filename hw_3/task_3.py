from random import random

#* Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

def fract_part_diff(lst: list, round_to: int = 2) -> float:
    # Если надо, чтобы работало с учетом 5.0 и т.п. то в if выражение будет такое:
    # if '.' in str(el)
    lst_fract = [round(el % 1, round_to) for el in lst if int(el) != el]

    # Без list comprehension

    # lst_fract = []

    # for el in lst:
    #     if int(el) != el:
    #         lst_fract.append(round(el % 1, round_to))

    print(f'Fractional parts, rounded to {round_to} digits:', lst_fract, sep='\n', end='\n\n')

    # Без функций max и min

    # max_el = 0
    # min_el = 1

    # for i in range(len(lst_fract)):
    #     if lst_fract[i] > max_el:
    #         max_el = lst_fract[i]

    #     if lst_fract[i] < min_el:
    #         min_el = lst_fract[i]

    # return round(max_el - min_el, round_to + 1)

    return round(max(lst_fract) - min(lst_fract), round_to + 1) if lst_fract else -1


# number_els = int(input('Enter the number of elements: '))
# Если хочется вводить ручками)

# lst_in = []

# for i in range(number_els):
#     lst_in.append(float(input(f'Enter the {i+1} element: ')))


# Если не хочется вводить ручками))))

# lst_in = [round(random() * 100, 2) for _ in range(number_els)]


# Примеры с сайта
lst_in = [1.1, 1.2, 3.1, 5, 10.01] # -> 0.19


print('Full list:', lst_in, sep='\n', end='\n\n')

fract_diff = fract_part_diff(lst_in)
print('Differnce between maximal and minimal fractional parts:', fract_diff)
