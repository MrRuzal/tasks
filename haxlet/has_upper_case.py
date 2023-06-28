def has_upper_case(text: str):
    return text != text.lower()


if __name__ == "__main__":
    print(has_upper_case(''))  # False
    print(has_upper_case('python'))  # False
    print(has_upper_case('pyThon'))  # True
