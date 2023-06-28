class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_count = 0

    def put(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size_count += 1

    def get(self):
        if self.head is None:
            print("error")
        else:
            value = self.head.value
            self.head = self.head.next
            self.size_count -= 1
            print(value)

    def size(self):
        print(self.size_count)


num_commands = int(input())
queue = LinkedListQueue()

for _ in range(num_commands):
    command = input().split()
    if command[0] == "put":
        queue.put(int(command[1]))
    elif command[0] == "get":
        queue.get()
    elif command[0] == "size":
        queue.size()
