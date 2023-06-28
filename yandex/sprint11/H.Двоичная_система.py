from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    if first_number == '0' and second_number == '0':
        return '0'
    sum = int(first_number, 2) + int(second_number, 2)
    result = []
    while sum:
        result.append(str(sum % 2))
        sum //= 2
    result.reverse()
    return ''.join(result)


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
