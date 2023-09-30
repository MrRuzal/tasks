# Дан список:
# [1, 2, 3, 4, 5, 6]
# Получите из него следующий срез:
# [1, 2, 3]


def list_number(numbers):
    return numbers[0:3]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6]
    print(list_number(numbers))
