# Дана строка:
# 'abcdef'
# Получите первых три символа этой строки:
# 'abc'


def slice_string(string):
    return string[:3]


if __name__ == '__main__':
    print(slice_string('abcdef'))
