letters_by_number = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


def combination(number, current_combination=''):
    if len(number) == 0:
        print(current_combination, end=' ')
    else:
        letters = letters_by_number.get(int(number[0]), '')
        for letter in letters:
            combination(number[1:], current_combination + letter)


if __name__ == '__main__':
    combination(number=list(input()))
