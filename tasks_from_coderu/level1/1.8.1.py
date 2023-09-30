# Дан кортеж с числами:
# (1, 2, 3, 4, 5)
# Найдите сумму элементов этого кортежа.


def sum_items(set_number):
    result = 0
    for number in list(set_number):
        result += number
    return result


if __name__ == '__main__':
    print(sum_items(set_number=(1, 2, 3, 4, 5)))
