# Сортировка выбором.


def select_sort(input_list):
    list_length = len(input_list)
    for current_index in range(list_length):
        min_index = current_index
        for index in range(current_index + 1, list_length):
            if input_list[index] < input_list[min_index]:
                min_index = index
        if min_index != current_index:
            input_list[current_index], input_list[min_index] = (
                input_list[min_index],
                input_list[current_index],
            )
    return input_list


if __name__ == '__main__':
    sorted_list = select_sort([-3, 5, 0, -8, 1, 10])
    print(sorted_list)
