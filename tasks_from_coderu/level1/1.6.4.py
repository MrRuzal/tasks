# Дан список с числами:
# [1, 2, -3, 4, -5]
# Найдите сумму положительных элементов этого списка.


def sum_items(list_numbers):
    result = []
    for number in list_numbers:
        if number > 0:
            result.append(number)
    return sum(result)


if __name__ == '__main__':
    print(sum_items(list_numbers=[1, 2, -3, 4, -5]))
