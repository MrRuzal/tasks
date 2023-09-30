# Быстрая сортировка.
# функция quick_sort() должна выполнить быструю сортировку списка.


def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    item = input_list[0]
    left = list(filter(lambda x: x < item, input_list))
    center = [i for i in input_list if i == item]
    right = list(filter(lambda x: x > item, input_list))
    return quick_sort(left) + center + quick_sort(right)


if __name__ == '__main__':
    print(quick_sort([7, 6, 10, 5, 9, 7, 8, 3, 4]))
