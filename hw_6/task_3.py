#* Дан список, вывести отдельно буквы и цифры, пользуясь filter

num_in = input('Enter a number: ')

# Так проще лично для меня)
# digs_sum = sum(int(el) for el in num_in if el.isdigit())

digs_sum = sum(map(int, filter(lambda el: el.isdigit(), num_in)))

print(digs_sum)