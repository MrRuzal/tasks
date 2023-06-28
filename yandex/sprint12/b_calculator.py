# contest ID 87993580
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError("Стек пуст")


def calculate(items, converter=int, stack=None, operations=OPERATIONS):
    stack = Stack() if stack is None else stack
    for item in items:
        try:
            stack.push(converter(item))
        except ValueError:
            operand_2, operand_1 = stack.pop(), stack.pop()
            if item in operations:
                stack.push(operations[item](operand_1, operand_2))
            else:
                raise ValueError(f"Недопустимый операнд или оператор: {item}")
    return stack.pop()


if __name__ == '__main__':
    print(calculate(input().split()))
