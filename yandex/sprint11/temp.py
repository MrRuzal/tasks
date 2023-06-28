# import sys

# def main():
#     num_lines = int(input())  # Считываем первую строку из потока ввода
#     output_numbers = []
#     for i in range(num_lines):
#         line = sys.stdin.readline().rstrip()
#         value_1, value_2 = line.split()
#         value_1 = int(value_1)
#         value_2 = int(value_2)
#         result = value_1 + value_2
#         output_numbers.append(str(result))
#     print('\n'.join(output_numbers))

# if __name__ == '__main__':
#     main()


def receiving_data():
    k = int(input()) * 2
    button_set = [input().replace('.', '') for _ in range(4)]
    return k, button_set


def data_processing(k, button_set):
    numbers = {}

    for row in button_set:
        for number in row:
            if number.isdigit():
                numbers[int(number)] += 1

    return sum(1 for count in numbers.values() if count <= k)


if __name__ == '__main__':
    k, button_set = receiving_data()
    print(data_processing(k, button_set))
