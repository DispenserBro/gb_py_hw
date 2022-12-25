from random import randint

#* Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

def get_list_unique(lst: list) -> list:
    # Классический вариант

    # lst_unique = []

    # for number in lst:
    #     if lst.count(number) > 1:
    #         continue

    #     lst_unique.append(number)


    # Через list comprehension

    lst_unique = [el for el in lst if lst.count(el) == 1]

    return lst_unique


number_els = int(input('Enter the number of elements: '))
# Если хочется вводить ручками)

# lst_in = []

# for i in range(number_els):
#     lst_in.append(int(input(f'Enter the {i+1} element: ')))
#     lst_in.append(float(input(f'Enter the {i+1} element: ')))


# Если не хочется вводить ручками))))

# max_number = int(input('Enter the max number: '))

# lst_in = [randint(0, max_number) for _ in range(number_els)]


# Примеры с сайта
lst_in = [3, 1, 2, 3] # -> 2 1

print('Full list:', lst_in, sep='\n')

print('Unique elements:', *get_list_unique(lst_in)) # Чтобы прям совсем по условию подходило его можно и развернуть)
