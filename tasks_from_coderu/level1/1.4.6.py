# Дан список:
# [1, 2, 3, 4, 5, 6]
# Получите из него два последних элемента:
# [5, 6]


def slice_numbers(numbers):
    return numbers[-2:]


if __name__ == '__main__':
    print(slice_numbers(numbers=[1, 2, 3, 4, 5, 6]))
