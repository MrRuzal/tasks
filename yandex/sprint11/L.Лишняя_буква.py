from typing import Tuple
from collections import Counter

def get_excessive_letter(shorter: str, longer: str) -> str:
    shorter_count = Counter(shorter)
    longer_count = Counter(longer)

    for char in longer_count:
        if shorter_count[char] != longer_count[char]:
            return char

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))