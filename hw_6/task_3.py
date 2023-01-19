#* Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

num_in = input('Enter a number: ')

# Так проще лично для меня)
# digs_sum = sum(int(el) for el in num_in if el.isdigit())

digs_sum = sum(map(int, filter(lambda el: el.isdigit(), num_in)))

print(digs_sum)