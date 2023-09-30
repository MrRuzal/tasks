# Дан словарь:
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Найдите сумму квадратов элементов этого словаря.


def sum_items(dict_items):
    result = 0
    for item in dict_items.values():
        result += item**2
    return result


if __name__ == '__main__':
    print(
        sum_items(
            dict_items={
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
            }
        )
    )
