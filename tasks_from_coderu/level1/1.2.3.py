# Дано число. Выведите в консоль сумму первой и последней цифры этого числа.


def sum_number(number):
    return int(str(number)[0]) + int(str(number)[-1])


if __name__ == '__main__':
    print(sum_number(535))
    print(sum_number(456))
    print(sum_number(31516))
