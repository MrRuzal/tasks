# Сортировка пузырьком.
# Дается список чисел на вход, нужно отсортирвоать пузырьком.


def bubble_sorting(input_list, n):
    if len(input_list) <= 1:
        return input_list
    count = 0
    for run in range(len(input_list) - 1):
        for index in range(len(input_list) - 1 - run):
            if input_list[index] == input_list[index + 1]:
                continue
            elif input_list[index] > input_list[index + 1]:
                count += 1
                input_list[index], input_list[index + 1] = (
                    input_list[index + 1],
                    input_list[index],
                )

    print('Отсортированный массив:', *input_list)
    print('Количество замен:', count)


if __name__ == '__main__':
    bubble_sorting(input_list=[5, 7, 4, 3, 8, 2], n=6)
    bubble_sorting(input_list=[5, 7, -4], n=3)
    bubble_sorting(input_list=[5, 7, 4, 1, 3, 8, 6, 2], n=8)
    bubble_sorting(input_list=[5, 7, 4, 3, 1, 3, 8, 6, 2], n=9)
