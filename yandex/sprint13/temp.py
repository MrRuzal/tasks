def find_bicycles_days(n, savings, bicycle_cost):
    left = 0
    right = n - 1
    first_bicycle_day = -1
    while left <= right:
        mid = (left + right) // 2
        if savings[mid] >= bicycle_cost:
            first_bicycle_day = mid + 1
            right = mid - 1
        else:
            left = mid + 1

    left = 0
    right = n - 1
    first_two_bicycles_day = -1
    while left <= right:
        mid = (left + right) // 2
        if savings[mid] >= 2 * bicycle_cost:
            first_two_bicycles_day = mid + 1
            right = mid - 1
        else:
            left = mid + 1

    return first_bicycle_day, first_two_bicycles_day


if __name__ == '__main__':
    n = int(input())
    savings = list(map(int, input().split()))
    bicycle_cost = int(input())

    result = find_bicycles_days(n, savings, bicycle_cost)
    print(*result)
