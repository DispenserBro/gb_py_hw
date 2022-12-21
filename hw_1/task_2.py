#* Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# from itertools import product


def de_morgan_law(x, y, z):
    left_part = not (x or y or z)
    right_part = (not x) and (not y) and (not z) # Скобки просто для удобства чтения
    return left_part == right_part

# combinations = product([0, 1], [0, 1], [0, 1])

# for combination in combinations:
#     print(f'{combination} -> {de_morgan_law(combination[0], combination[1], combination[2])}')

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'({x}, {y}, {z}) -> {de_morgan_law(x, y, z)}')
