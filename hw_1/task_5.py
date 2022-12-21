#* Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
from math import floor


def calculate_distance(point_1, point_2, sign_digs=2):
    dx = abs(point_1[0] - point_2[0])
    dy = abs(point_1[1] - point_2[1])

    return int(((dx ** 2 + dy ** 2) ** 0.5) * 10 ** sign_digs) / 10 ** sign_digs
# Считаю, что первый пример работы на сайте выполнен не совсем правильно (5.09 без этих извращений не получить)
# На всякий случай, (7,-5) -> (1,-1) = 5.09901......



first_point = int(input('Введите х 1 точки: ')), int(input('Введите у 1 точки: '))
second_point = int(input('Введите х 2 точки: ')), int(input('Введите у 2 точки: '))

print(f'Расстояние между точками {first_point} и {second_point} равно \
{calculate_distance(first_point, second_point)}')
