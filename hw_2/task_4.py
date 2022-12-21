#* Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно

num_n = int(input('Enter the number: '))

# С полным списком чисел

# lst_nums = list(range(1, num_n + 1))

# print('Generated list:', lst_nums, sep='\n', end='\n\n')

# print('Sum of even numbers:', sum(lst_nums[1::2]))

# # С учетом отрицательных чисел

if num_n <= 0:
    lst_nums = list(range(num_n, 2))
    print('Generated list:', lst_nums, sep='\n', end='\n\n')
    print('Sum of even numbers:', sum(lst_nums[-2::-2]))
else:
    lst_nums = list(range(1, num_n + 1))
    print('Generated list:', lst_nums, sep='\n', end='\n\n')
    print('Sum of even numbers:', sum(lst_nums[1::2]))

# Со списком только четных чисел

# lst_nums = list(range(0, num_n + 1, 2))

# print('Sum of even numbers:', sum(lst_nums))
