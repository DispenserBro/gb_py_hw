#* Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой,
# сколько указал пользователь(БЕЗ round())


from decimal import Decimal, getcontext
# Стандартное решение дает результат до 15 знака после запятой
# import math

# Очень сложно объяснить, тут используется алгоритм Чудновского (без использования факториала)
# Такое врое как проходят на первом курсе присладной математики, если мне память не изменяет))))
# Cам я просто скопипастил с https://habr.com/ru/post/309674/
# С доработкой до 3 питона и допиливанием некоторых мелочей

def chudnovsky2(digs: int) -> Decimal:
    pi = Decimal(13591409)
    a_k = Decimal(1)
    k = 1

    while k < digs:
        a_k *= -Decimal((6 * k - 5) * (2 * k - 1) * (6 * k - 1)) \
              / Decimal(k * k * k * 26680 * 640320 * 640320)

        val = a_k * (13591409 + 545140134 * k)

        pi += val
        k += 1

    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi ** (-1)

    return pi


# Значение по умолчанию для малых знаков (<= 100)
# Скорость удовлетворительная для этого количества (< 0.02 сек в зависимости от свободной оперативки)
default_digits = 100

# Увеличение буфера для хранения знаков в Decimal
getcontext().prec = default_digits + 5
# Экспериментально проверил, что погрешность чаще всего исчезает при таких значениях
# [:-3] для учета знаков "3."
chudnovsky_pi = str(chudnovsky2(default_digits + 5))[:-3]
# print(chudnovsky_pi[:17]) == print(math.pi)

decm_places = int(input('Enter the number of decimal places of Pi: '))

if decm_places == 0:
    print(chudnovsky_pi[0])

elif decm_places < 0:
    print('Wrong number of decimal places!')

elif decm_places > default_digits:
    getcontext().prec = decm_places + 5
    chudnovsky_pi = str(chudnovsky2(default_digits + 5))[:-3]
    print(chudnovsky_pi)

else:
    print(chudnovsky_pi[:decm_places + 2])
