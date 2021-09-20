# Есть словарь dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
# Составить из него новый словарь, содержащий только те элементы, у которых
# значение больше или равно 3.

def new_custom_dict(d):
    new_dict = {}
    for key, val in d.items():
        if val >= 3:
            new_dict[key] = val
    return new_dict


dictt = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
print(new_custom_dict(dictt))
