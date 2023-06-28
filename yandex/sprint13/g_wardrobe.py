def color_sort(array):
    pink = []
    yellow = []
    raspberry = []
    for i in array:
        if i == 0:
            pink.append(i)
        if i == 1:
            yellow.append(i)
        if i == 2:
            raspberry.append(i)
    return pink + yellow + raspberry


if __name__ == '__main__':
    quantity = int(input())
    print(*color_sort(array=list(map(int, input().split()))))

# def color_sort(array):
#     colors = {0: [], 1: [], 2: []}
#     for i in array:
#         if i in colors:
#             colors[i].append(i)
#     return colors[0] + colors[1] + colors[2]


# if __name__ == '__main__':
#     quantity = int(input())
#     print(*color_sort(array=list(map(int, input().split()))))