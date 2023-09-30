# Дан словарь:
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Найдите сумму элементов этого словаря.


def sum_items(dict_items):
    return sum(dict_items.values())


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
