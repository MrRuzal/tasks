# Дано некоторое число:
# 12345
# Получите список цифр этого числа.


def list_letters(number):
    return [int(digit) for digit in str(number)]


if __name__ == '__main__':
    print(list_letters(number=12345))
