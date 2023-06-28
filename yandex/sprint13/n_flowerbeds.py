def flowerbeds(array):
    data = sorted([t for t in (set(tuple(i) for i in array))])
    result = []
    start = data[0][0]
    end = data[0][1]
    for i in range(0, len(data) - 1):
        if data[i + 1][0] > end:
            result.append([start, end])
            start = data[i + 1][0]
            end = data[i + 1][1]
        else:
            if data[i + 1][1] <= end:
                continue
            else:
                end = data[i + 1][1]
    result.append([start, end])
    for i in result:
        print(*i, sep=' ')


if __name__ == '__main__':
    quantity = int(input())
    flowerbeds(
        array=[list(map(int, input().split())) for _ in range(quantity)]
    )
