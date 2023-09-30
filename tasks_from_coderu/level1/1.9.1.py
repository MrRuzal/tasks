# 'abcdef'
# Получите три последних символа этой строки:
# 'def'


def slice_string(string):
    return string[-3:]


if __name__ == '__main__':
    print(slice_string('abcdef'))
