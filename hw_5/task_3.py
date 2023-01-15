import os.path
from pathlib import Path

#* Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных


def compress_rle(str_in: str) -> str:
    count = 1
    res = ''

    for i in range(len(str_in) - 1):
        if str_in[i] == str_in[i + 1]:
            count += 1

        else:
            res += f'{count}{str_in[i]}'
            count = 1

    if count > 1 or str_in[-2] != str_in[-1]:
        res += f'{count}{str_in[i]}'

    return res


def decompress_rle(in_str: str) -> str:
    number = ''
    res = ''
    for i in range(len(in_str)):
        if in_str[i].isdigit():
            number += in_str[i]
        else:
            res += in_str[i] * int(number)
            number = ''
    return res


# Правильный путь до папки с файлом
BASE_DIR = Path(__file__).resolve().parent

with open(os.path.join(BASE_DIR, 'input_data.txt'), 'r') as f:
    in_data = f.read()

in_comp = compress_rle(in_data)
print(in_comp)

in_decomp = decompress_rle(in_comp)
print(in_decomp)

# Проверка на всякий пожарный)
# print(in_decomp == in_data)