# Дана строка. Если в этой строке более одного символа,
# выведите в консоль предпоследний символ этой строки.


def last_character(string):
    return string[-2]


if __name__ == '__main__':
    print(last_character('test string'))  # n
    print(last_character('hello'))  # l
