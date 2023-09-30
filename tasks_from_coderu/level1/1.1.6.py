# Дано слово. Получите его последнюю букву.
# Если слово заканчивается на мягкий знак, то получите предпоследнюю букву.


def last_letter(string):
    if string[-1] == 'ь':
        return string[-2]
    return string[-1]


if __name__ == '__main__':
    print(last_letter('сказать'))
    print(last_letter('кино'))
