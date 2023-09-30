# Сортировка вставками.


def insertion_sorting(input_list):
    for current_index in range(len(input_list)):
        for sorted_index in range(current_index, 0, -1):
            if input_list[sorted_index] < input_list[sorted_index - 1]:
                input_list[sorted_index], input_list[sorted_index - 1] = (
                    input_list[sorted_index - 1],
                    input_list[sorted_index],
                )
            else:
                break
    return input_list


if __name__ == '__main__':
    print(*insertion_sorting([-3, 5, 0, -8, 1, 10]))  # -8 -3 0 1 5 10
