# def big_num(n, array):
#     for i in range(0, n - 1):
#         if (str(array[i]) + str(array[i + 1])) < (
#             str(array[i + 1]) + str(array[i])
#         ):
#             array[i], array[i + 1] = array[i + 1], array[i]
#             return big_num(n, array)
#     return array
# def big_num(n, array):
#     iteration = 0
#     swapped = True

#     while swapped and iteration < n - 1:
#         swapped = False
#         for i in range(n - 1):
#             if str(array[i]) + str(array[i + 1]) < str(array[i + 1]) + str(
#                 array[i]
#             ):
#                 array[i], array[i + 1] = array[i + 1], array[i]
#                 swapped = True
#         iteration += 1

#     return array
MAX_RECURSION_DEPTH = 1000


def big_num(n, array, recursion_depth=0):
    if recursion_depth > MAX_RECURSION_DEPTH:
        return array
    swapped = False
    for i in range(n - 1):
        if str(array[i]) + str(array[i + 1]) < str(array[i + 1]) + str(
            array[i]
        ):
            array[i], array[i + 1] = array[i + 1], array[i]
            swapped = True
    if swapped:
        return big_num(n, array, recursion_depth + 1)
    return array


if __name__ == '__main__':
    n = int(input())
    result = big_num(n, array=list(map(int, input().split())))
    print(''.join(map(str, result)))
