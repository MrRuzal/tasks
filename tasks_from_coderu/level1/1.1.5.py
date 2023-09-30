# Даны два слова. Проверьте, что первые буквы этих слов совпадают.


def two_words(one, two):
    if one[0:1] == two[0:1]:
        return 'Совпадают'
    return 'Не совпадают'


if __name__ == '__main__':
    print(
        two_words(
            one='hello',
            two='Python',
        )
    )
    print(
        two_words(
            one='hello',
            two='hard',
        )
    )
