def is_power_of_four(number: int) -> bool:
    temp = 1
    while temp < number:
        temp *= 4
    return temp == number


print(is_power_of_four(int(input())))
