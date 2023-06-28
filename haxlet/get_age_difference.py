def get_age_difference(first_birthday: int, second_birthday: int):
    return f"The age difference is {abs(first_birthday - second_birthday)}"


if __name__ == '__main__':
    actual = get_age_difference(2001, 2018)
    print(actual)
