# Дано число. Выведите в консоль первую цифру этого числа.


def first_number(number):
    return str(number)[0]


if __name__ == '__main__':
    print(first_number(780))  # 7
    print(first_number(1880))  # 1
