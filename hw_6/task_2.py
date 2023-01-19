#* Дан список, вывести отдельно буквы и цифры, пользуясь filter

# Входной список может быть подан и иначе
lst_in = [12,'sadf',5643] # ---> ['sadf'] ,[12,5643]

# list comprehension
# lst_nums = [el for el in lst_in if type(el) == int]
# lst_strs = [el for el in lst_in if type(el) == str]

lst_nums = list(filter(lambda el: type(el) == int, lst_in))
lst_strs = list(filter(lambda el: type(el) == str, lst_in))

print(lst_strs, lst_nums, sep=', ')