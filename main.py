my_list = [42, 43]
my_dict = {
    'foo': {
        'a': 12,
        'b': (1, 2, 3, 4, my_list)
    },
    'bar': {
        'c': 12,
        'd': {5, 6, 7, 8}
    },
    'moo': {
        'e': 12,
        'f': {'Lol': ['L', 'o', 'l']}
    },
}

print(my_dict['bar']['d'])
my_dict['moo']['f']['Lol'].pop(1)
my_dict['moo']['f']['K'] = ['K', 'e', 'k']
# print(my_dict)
my_dict.clear()
# print(my_dict)