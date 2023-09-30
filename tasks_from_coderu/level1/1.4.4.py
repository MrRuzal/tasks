# Выведите в консоль все четные числа из промежутка от 1 до 100.


def even_numbers():
    for number in range(1, 101):
        if number % 2 == 0:
            print(number)


if __name__ == '__main__':
    even_numbers()
