# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1

num_n = int(input('Enter the number: '))

i = 1

while i <= abs(num_n):
    i = i + 1

    if not num_n % i:
        break
else:
    i = abs(num_n)

print(f'The smallest divisor for {num_n} is {i}')