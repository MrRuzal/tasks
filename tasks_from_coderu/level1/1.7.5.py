# Дано некоторое число:
# 12345
# Переверните его:
# 54321


def reverse(number):
    list_number = [int(digit) for digit in str(number)]
    return int(''.join(map(str, list(reversed(list_number)))))


if __name__ == '__main__':
    print(reverse(number=12345))
