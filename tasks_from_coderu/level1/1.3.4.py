# Дан список:
# [1, 2, 3, 4, 5, 6]
# Получите из него следующий срез:
# [3, 4, 5]


def list_numbers(numbers):
    return numbers[2:-1]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6]
    print(list_numbers(numbers))
