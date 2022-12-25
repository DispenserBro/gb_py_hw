#* Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

def prime_factors(number: int) -> list:
    number = abs(number)
    i = 2
    factors = []

    while i * i <= number:
        if number % i:
            i += 1

        else:
            number //= i
            factors.append(i)

    if number > 1:
        factors.append(number)

    return factors

number_to_decompose = int(input('Enter a number to decompose: '))
number_farctors = prime_factors(number_to_decompose)
print('Decomposed number:')
print(number_to_decompose, '=', ' * '.join(map(str, number_farctors)))
