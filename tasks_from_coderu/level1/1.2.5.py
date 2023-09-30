# Даны два числа. Проверьте, что первые цифры этих чисел совпадают.


def first_numbers(one, two):
    if str(one)[0] == str(two)[0]:
        return 'Совпадают'
    return 'Не совпадают'


if __name__ == '__main__':
    print(first_numbers(135, 5548))
    print(first_numbers(885, 5548))
    print(first_numbers(535, 558))
