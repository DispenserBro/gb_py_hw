# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится)

x_coord = int(input('Введите х точки: '))
y_coord = int(input('Введите у точки: '))

if (not x_coord) and y_coord:
    print(f'Точка ({x_coord}, {y_coord}) лежит на оси Х')
elif (not y_coord) and x_coord:
    print(f'Точка ({x_coord}, {y_coord}) лежит на оси Y')
elif x_coord > 0:
    if y_coord > 0:
        print(f'Точка ({x_coord}, {y_coord}) находится в I четверти')
    else:
        print(f'Точка ({x_coord}, {y_coord}) находится в IV четверти')
elif x_coord < 0:
    if y_coord > 0:
        print(f'Точка ({x_coord}, {y_coord}) находится во II четверти')
    else:
        print(f'Точка ({x_coord}, {y_coord}) находится в III четверти')
else:
    print(f'Координаты не должны одновременно быть равны 0!')
