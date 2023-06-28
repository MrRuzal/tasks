def satisfied_count(greed, cookies_size):
    result = 0
    cookie_index = 0
    greed_sorted = sorted(greed)
    cookies_sorted = sorted(cookies_size)
    for i in greed_sorted:
        while cookie_index < len(cookies_sorted):
            if cookies_sorted[cookie_index] >= i:
                result += 1
                cookie_index += 1
                break
            cookie_index += 1
    return result


if __name__ == '__main__':
    children_count = input()
    greed = list(map(int, input().split()))
    cookies_count = input()
    cookies_size = list(map(int, input().split()))
    print(satisfied_count(greed, cookies_size))
