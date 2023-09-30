# Дано число. Выведите в консоль последнюю цифру этого числа.


def first_number(number):
    return str(number)[-1]


if __name__ == '__main__':
    print(first_number(780))  # 0
    print(first_number(1881))  # 1
