# Найдите сумму всех целых нечетных чисел в промежутке от 1 до 100.


def even_integers():
    result = 0
    for number in range(1, 101):
        if not number % 2 == 0:
            result += number
    print(result)


if __name__ == '__main__':
    even_integers()
