# Дан список с числами:
# [-1, 2, -3, 4, 5, 11]
# Найдите сумму тех элементов этого списка,которые больше нуля и меньше десяти.


def sum_items(list_numbers):
    result = []
    for number in list_numbers:
        if 0 < number < 10:
            result.append(number)
    return sum(result)


if __name__ == '__main__':
    print(sum_items(list_numbers=[-1, 2, -3, 4, 5, 11]))
