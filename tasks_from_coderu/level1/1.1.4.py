# Дано число. Проверьте, четное оно или нет.


def even_number(num):
    if num % 2 == 0:
        return 'Число четное'
    return 'Число не четное'


if __name__ == '__main__':
    print(even_number(1))
    print(even_number(2))
    print(even_number(3))
    print(even_number(4))
    print(even_number(5))
    print(even_number(6))
