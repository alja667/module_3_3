def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [987, 64, 329]
values_dict = {'a': [2, 3, 7, 8, 9, 4, 000, 2, 0, ], 'b': 'strit', 'c': 2034}
values_list_2 = ['эх', 78887]

print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
