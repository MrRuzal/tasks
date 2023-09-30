# Дан словарь с числами:
# {
# 	'a': 1,
# 	'b': 2,
# 	'c': 3,
# 	'd': 4,
# }
# Увеличьте каждое число из словаря в 2 раза:
# {
# 	'a': 2,
# 	'b': 3,
# 	'c': 6,
# 	'd': 8,
# }


def increase(numbers_dict):
    for key in numbers_dict:
        numbers_dict[key] *= 2
    print(numbers_dict)


if __name__ == '__main__':
    increase(
        numbers_dict={
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
        }
    )
