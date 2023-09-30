# Дано число. Проверьте, отрицательное оно или нет.
# Выведите об этом информацию в консоль.


def trivial_number(num):
    if num < 0:
        return 'Число отрицательное'
    return 'Число не отрицательное'


if __name__ == '__main__':
    print(trivial_number(5))
    print(trivial_number(-5))
    print(trivial_number(-3))
    print(trivial_number(30))
