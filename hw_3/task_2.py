from random import randint

#* Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д

def product_of_pairs(lst: list) -> list:
    res_lst = []

    for i in range(len(lst) // 2 + len(lst) % 2):
        res_lst.append(lst[i] * lst[-(i + 1)])

    return res_lst


# number_els = int(input('Enter the number of elements: '))
# Если хочется вводить ручками)

# lst_in = []

# for i in range(number_els):
#     lst_in.append(int(input(f'Enter the {i+1} element: ')))
#     lst_in.append(float(input(f'Enter the {i+1} element: ')))


# Если не хочется вводить ручками))))

# max_number = int(input('Enter the max number: '))

# lst_in = [randint(0, max_number) for _ in range(number_els)]


# Примеры с сайта
# lst_in = [2, 3, 4, 5, 6] # -> [12, 15, 16]
lst_in = [2, 3, 5, 6] # -> [12, 15]


print('Full list:', lst_in, sep='\n')

prod_result = product_of_pairs(lst_in)
print(f'Products of pairs:', prod_result, sep='\n')
