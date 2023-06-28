class MyQueueSized:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def push(self, x):
        if len(self.queue) < self.max_size:
            self.queue.append(x)
        else:
            print("error")

    def pop(self):
        if self.queue:
            print(self.queue.pop(0))
        else:
            print("None")

    def peek(self):
        if self.queue:
            print(self.queue[0])
        else:
            print("None")

    def size(self):
        print(len(self.queue))


num_commands = int(input())
max_size = int(input())
queue = MyQueueSized(max_size)

for _ in range(num_commands):
    command = input().split()
    if command[0] == "push":
        queue.push(int(command[1]))
    elif command[0] == "pop":
        queue.pop()
    elif command[0] == "peek":
        queue.peek()
    elif command[0] == "size":
        queue.size()
