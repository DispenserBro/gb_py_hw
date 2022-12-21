#* Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

# Рекурсивная ф-я все проблемы рекурсии

# def fib(number: int) -> int:
#     if number > -1:
#         if number == 0:
#             return 0
#         elif number == 1:
#             return 1
#         else:
#             return fib(number - 1) + fib(number - 2)
#     else:
#         return int((-1) ** (number + 1) * fib(-number))


# Линейная функция через формулу Бине, точность теряется при n > 71
# Но при этом в разы быстрее при росте чисел, и это логично)
# Про формулу Бине можно почитать на вики: https://ru.wikipedia.org/wiki/Числа_Фибоначчи#Формула_Бине

def fib(number:int) -> int:
    if number > -1:
        if number == 0:
            return 0
        else:
            return int((((5 ** 0.5 + 1) / 2) ** number - ((1 - 5 ** 0.5) / 2) ** number)/ 5 ** 0.5)
    else:
        return int((-1) ** (number + 1) * ((((5 ** 0.5 + 1) / 2) ** -number - ((1 - 5 ** 0.5) / 2) ** -number)/ 5 ** 0.5))

def two_side_fib(num_k: int) -> list[int]:
    fib_lst = [fib(number) for number in range(-num_k, num_k + 1)]

    return fib_lst


# print(two_side_fib(71))
indx_range = int(input('Enter the number to get Fibonacci list in range [-n, n](n>=0): '))
print(two_side_fib(indx_range))
