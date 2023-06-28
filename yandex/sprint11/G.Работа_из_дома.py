def to_binary(number: int) -> str:
    if number == 0:
        return 0
    result = []
    while number:
        result.append(str(number % 2))
        number //= 2
    result.reverse()
    return ''.join(result)


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
