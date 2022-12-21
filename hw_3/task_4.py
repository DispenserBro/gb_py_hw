#* Напишите программу, которая будет преобразовывать десятичное число в двоичное

def decimal_to_binary(number: int) -> str | int:
    # Только строки

    # result = ''

    # while number > 0:
    #     result = str(number % 2) + result
    #     number //= 2


    # Cписок строк (где ## - с разворотом списка)

    # result = []
    # while number > 0:
    #     # result.append(str(number % 2))
    #     result.insert(0, str(number % 2))
    #     number //= 2

    # # result.reverse()

    # result = ''.join(result)


    # Числа

    result = 0
    power = 0

    while number > 0:
        result = (number % 2) * (10 ** power) + result # Скобки чисто для читаемости)
        number //= 2
        power += 1

    return result

# Примеры с сайта
print(decimal_to_binary(45)) # -> 101101
print(decimal_to_binary(3)) # -> 11
print(decimal_to_binary(2)) # -> 10
