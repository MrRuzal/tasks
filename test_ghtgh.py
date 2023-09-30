def transformation(string, dictionary):
    result = ''
    for word_string in string.split(' '):
        for word_dictionary in dictionary:
            if word_dictionary.lower() in word_string.lower():
                result += '.'
            elif word_dictionary.lower() not in word_string.lower():
                result += '~'
            elif ',' or ' ' in word_string:
                result += '.'
    return result


if __name__ == '__main__':
    # string = input()
    string = 'Now I am become death, the destroyer of worlds'
    # n = 4
    # dictionary = input()
    dictionary = ['I', 'become', 'Death', 'Worlds']
    print(transformation(string, dictionary))
