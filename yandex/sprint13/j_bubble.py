def bubble_sort(array):
    length_array = len(array)
    was_changed = False
    while True:
        swapped = False
        for i in range(0, length_array - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                was_changed = True
        if swapped:
            print(' '.join(map(str, array)))
        else:
            break
    if not was_changed:
        print(' '.join(map(str, array)))


if __name__ == '__main__':
    n = int(input())
    bubble_sort(array=list(map(int, input().split())))
