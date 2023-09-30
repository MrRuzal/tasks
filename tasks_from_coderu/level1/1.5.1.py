# Найдите сумму всех целых чисел от 1 до 100.


def sum_all_numbers():
    result = []
    for number in range(1, 101):
        result.append(number)
    print(sum(result))


if __name__ == '__main__':
    sum_all_numbers()
