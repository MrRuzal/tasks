# Выведите в консоль все числа кратные трем в промежутке от 1 до 100.


def multiples_of_three():
    for number in range(1, 101):
        if number % 3 == 0:
            print(number)


if __name__ == '__main__':
    multiples_of_three()
