class StackMaxEffective:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            return "error"
        x = self.stack.pop()
        if x == self.max_stack[-1]:
            self.max_stack.pop()
        return x

    def get_max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


stack = StackMaxEffective()
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        result = stack.pop()
        if result == "error":
            print(result)
    elif command[0] == "get_max":
        result = stack.get_max()
        if result is None:
            print("None")
        else:
            print(result)
