# Даны два целых числа.
# Проверьте, что первое число без остатка делится на второе.


def two_number(first, second):
    if first % second == 0:
        return 'Делится'
    return 'Не делится'


if __name__ == '__main__':
    print(two_number(100, 50))
    print(two_number(100, 60))
