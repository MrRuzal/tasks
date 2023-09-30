# Дан список с числами:
# [1, 2, 3, 4, 5]
# Найдите сумму квадратных корней элементов этого списка.


def sum_items(list_number):
    result = []
    for number in list_number:
        result.append(number**0.5)  # можно исаользовать math.sqrt(number)
    return sum(result)


if __name__ == '__main__':
    print(sum_items(list_number=[1, 2, 3, 4, 5]))
