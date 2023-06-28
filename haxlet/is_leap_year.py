def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if __name__ == '__main__':
    print(is_leap_year(2018))  # False
    print(is_leap_year(2017))  # False
    print(is_leap_year(2016))  # True
    print(is_leap_year(2000))  # True
