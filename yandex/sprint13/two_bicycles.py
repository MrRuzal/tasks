def bicycles(many, cost):
    n = len(many)
    left = 1
    right = n

    # Поиск первого дня для покупки одного велосипеда
    while left <= right:
        mid = (left + right) // 2
        if many[mid - 1] >= cost:
            right = mid - 1
        else:
            left = mid + 1

    if left > n or many[left - 1] < cost:
        # Вася не сможет купить ни одного велосипеда
        first_bike_day = -1
    else:
        first_bike_day = left

    left = 1
    right = n

    # Поиск первого дня для покупки двух велосипедов
    while left <= right:
        mid = (left + right) // 2
        if many[mid - 1] >= 2 * cost:
            right = mid - 1
        else:
            left = mid + 1

    if left > n or many[left - 1] < 2 * cost:
        # Вася не сможет купить два велосипеда
        return first_bike_day, -1
    else:
        return first_bike_day, left


if __name__ == '__main__':
    count_bicycles = int(input())
    print(
        *bicycles(many=[int(i) for i in input().split()], cost=int(input()))
    )
