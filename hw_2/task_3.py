from random import randint

#* Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете

num_n = int(input('Enter the number: '))

lst_nums = list(range(-abs(num_n), abs(num_n) + 1))

if num_n < 0:
    lst_nums.reverse()

number_els = 5

# Если хочется вводить ручками)

# lst_i = []

# for i in range(number_els):
#     lst_i.append(int(input(f'Enter the {i+1} element: ')))


# Если не хочется вводить ручками))))

lst_i = [randint(0, len(lst_nums) - 1) for _ in range(number_els)]

print('Generated list:', lst_nums, sep='\n', end='\n\n')
print('Indexes for multiplication:', lst_i, sep='\n', end='\n\n')

result = 1

for indx in lst_i:
    result *= lst_nums[indx]

print(f'Result: {result}')
