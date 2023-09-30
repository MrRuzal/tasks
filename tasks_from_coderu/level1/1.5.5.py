# Дан список:
# [1, 2, 3, 4, 5, 6]
# Получите из него каждый второй элемент:
# [1, 3, 5]


def second_item(input_list):
    result = []
    for index in range(0, len(input_list), 2):
        result.append(input_list[index])
    return result


if __name__ == '__main__':
    print(second_item(input_list=[1, 2, 3, 4, 5, 6]))
