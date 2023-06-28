# contest ID 87713699
from typing import List


def calculate_distances(street, target_value='0') -> List[int]:
    zeros = [
        index for index, value in enumerate(street) if value == target_value
    ]
    distances = [0] * len(street)
    first = zeros[0]
    distances[:first] = [first - pos for pos in range(first)]
    for left, right in zip(zeros, zeros[1:]):
        distances[left+1: right] = [
            min(pos - left, right - pos) for pos in range(left + 1, right)
        ]
    last = zeros[-1]
    distances[last+1:] = [
        pos - last for pos in range(last + 1, len(street))
    ]
    return distances


if __name__ == '__main__':
    input()
    print(*calculate_distances(input().split()))
