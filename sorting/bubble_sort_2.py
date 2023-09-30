# Сортировка пузырьком.


def bubble_sort(input_list):
    len_list = len(input_list)
    for i in range(len_list - 1):
        for j in range(len_list - 1 - i):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = (
                    input_list[j + 1],
                    input_list[j],
                )
    return input_list


if __name__ == '__main__':
    print(*bubble_sort([6, 8, 3, 4, 2, 1, 0]))
