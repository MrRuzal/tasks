# Дан список с числами:
# [1, 2, 3, 4, 5]
# Найдите сумму квадратов элементов этого списка.


def sum_items(list_number):
    result = []
    for number in list_number:
        result.append(number**2)
    return sum(result)


if __name__ == '__main__':
    print(sum_items(list_number=[1, 2, 3, 4, 5]))
