class StackMax:
    def __init__(self):
        self.main_stack = []
        self.track_stack = []

    def push(self, x):
        self.main_stack.append(x)
        if not self.track_stack or x >= self.track_stack[-1]:
            self.track_stack.append(x)

    def pop(self):
        if not self.main_stack:
            return None
        if self.main_stack[-1] == self.track_stack[-1]:
            self.track_stack.pop()
        return self.main_stack.pop()

    def get_max(self):
        if not self.track_stack:
            return None
        return self.track_stack[-1]


stack = StackMax()
n = int(input().strip())

for _ in range(n):
    command = input().strip().split()
    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        if stack.pop() is None:
            print("error")
    elif command[0] == "get_max":
        print(stack.get_max())
