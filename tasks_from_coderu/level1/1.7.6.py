# Дано некоторое число:
# 12345
# Найдите сумму цифр этого числа.


def list_letters(number):
    return sum(list(int(digit) for digit in str(number)))


if __name__ == '__main__':
    print(list_letters(number=12345))
