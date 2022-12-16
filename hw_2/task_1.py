from math import factorial as fact

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

num_n = int(input('Enter the number of elements: '))

# Без модуля math

lst_fact = []

for i in range(num_n):
    if i:
        new_el = 1

        for j in range(i + 1):
            new_el *= j + 1

        lst_fact.append(new_el)
    else:
        lst_fact.append(i + 1)

# С модулем math

# lst_fact = [fact(i + 1) for i in range(num_n)]

print(*lst_fact)
