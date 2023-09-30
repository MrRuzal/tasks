# Сортировка слиянием.


def merge_list(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]
    return result


def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list

    center = len(input_list) // 2
    left = merge_sort(input_list[:center])
    right = merge_sort(input_list[center:])
    return merge_list(left, right)


if __name__ == '__main__':
    print(*merge_sort([7, 5, 2, 3, 9, 8, 6]))  # 2 3 5 6 7 8 9
    print(*merge_sort([6, 2, 19, 5, 10, 7, 11]))  # 2 5 6 7 10 11 19
