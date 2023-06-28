def is_correct_bracket_seq(brackets):
    stack = []
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    brackets_map = {')': '(', '}': '{', ']': '['}
    for char in brackets:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != brackets_map[char]:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    print(is_correct_bracket_seq(input().strip()))


# def is_correct_bracket_seq(seq):
#     stack = []
#     opening_brackets = ['(', '{', '[']
#     closing_brackets = [')', '}', ']']
#     brackets_map = {')': '(', '}': '{', ']': '['}

#     for char in seq:
#         if char in opening_brackets:
#             stack.append(char)
#         elif char in closing_brackets:
#             if not stack or stack[-1] != brackets_map[char]:
#                 return False
#             stack.pop()

#     return len(stack) == 0

# # Чтение входной строки
# seq = input().strip()

# # Проверка правильности скобочной последовательности
# result = is_correct_bracket_seq(seq)

# # Вывод результата
# print(result)
