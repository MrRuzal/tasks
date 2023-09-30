# Дан список с числами:
# [1, 2, 3, 4, 5, 6]
# Увеличьте каждое число из списка на 10 процентов.


def percentage_increase(number_list):
    result = [x * 1.10 for x in number_list]
    return result


if __name__ == '__main__':
    print(percentage_increase(number_list=[1, 2, 3, 4, 5, 6]))
