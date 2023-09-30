# Дана некоторая строка:
# 'abcdeabc'
# Получите сет ее символов:
# {'a', 'b', 'c', 'd', 'e'}


def dictionary_conversion(string):
    return set(string)


if __name__ == '__main__':
    print(dictionary_conversion(string='abcdeabc'))
