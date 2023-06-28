from typing import List, Tuple, Optional

def twosum_with_sort(numbers, X):
    numbers.sort()

    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            return numbers[left], numbers[right]
        if current_sum < X:
            left += 1
        else:
            right -= 1
    return None, None
def read_input() -> Tuple[List[int], int]:
    n = int(input())
    numbers = list(map(int, input().strip().split()))
    X = int(input())
    return numbers, X

def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

numbers, X = read_input()
print_result(twosum_with_sort(numbers, X))