# v1
def letter_multiply(text: str, symdol: str, num: int) -> str:
    result: str = ''
    for item in text:
        if item == symdol:
            result += item * num
        else:
            result += item
    return result


if __name__ == "__main__":
    text = 'python'
    print(letter_multiply(text, 'p', 2))  # => ppython
    print(letter_multiply(text, 'y', 3))  # => pyyython
    print(letter_multiply(text, 'n', 4))  # => pythonnnn

# v2
# def letter_multiply(text: str, letter: str, count: int) -> str:
#     return text.replace(letter, letter * count)


# if __name__ == "__main__":
#     text = 'python'
#     print(letter_multiply(text, 'p', 2))  # => ppython
#     print(letter_multiply(text, 'y', 3))  # => pyyython
#     print(letter_multiply(text, 'n', 4))  # => pythonnnn
