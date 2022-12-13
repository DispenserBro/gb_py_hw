# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

entered_day = int(input('Введите номер дня: '))

# print(['нет', 'да'][entered_day % 7 == 0 or entered_day % 7 == 6])

if entered_day % 7 == 0 or entered_day % 7 == 6:
    print('да')
else:
    print('нет')
