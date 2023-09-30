# Дана некоторая строка:
# 'abcde'
# Переберите и выведите в консоль по очереди все символы с конца строки.


def characters_end_string(string):
    characters_list = reversed(list(string))
    for characters in characters_list:
        print(characters)


if __name__ == '__main__':
    characters_end_string(string='abcde')
