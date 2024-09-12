def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# Функция с параметрами по умолчанию:
print_params(b = 25)
print_params(c = [1,2,3])

# Распаковка параметров:
values_list = (2, 'столбец', False)
print_params(*values_list)
values_dict = {'a':'abc', 'b':False, 'c':23}
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = (54.32, 'Строка')
print_params(*values_list_2,42)
