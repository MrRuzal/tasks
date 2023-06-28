def is_palindrome(line: str) -> bool:
    alphanumeric = [ch.lower() for ch in line if ch.isalnum()]
    return alphanumeric == alphanumeric[::-1]


print(is_palindrome(input().strip()))
