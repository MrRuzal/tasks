# Дано число. Выведите количество цифр в этом числе.


def quantity_number(number):
    return len(str(number))


if __name__ == '__main__':
    print(quantity_number(131568))
    print(quantity_number(1313546568))
    print(quantity_number(1318))
