# contest ID 87993333
class Deque:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.front = 1
        self.back = 0
        self.count = 0

    def check_overflow(self):
        if self.count == self.size:
            raise IndexError('Дек переполнен')

    def check_empty(self):
        if self.count == 0:
            raise IndexError('Дек пуст')

    def push_back(self, value):
        self.check_overflow()
        self.back = (self.back + 1) % self.size
        self.buffer[self.back] = value
        self.count += 1

    def push_front(self, value):
        self.check_overflow()
        self.front = (self.front - 1) % self.size
        self.buffer[self.front] = value
        self.count += 1

    def pop_front(self):
        self.check_empty()
        value = self.buffer[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value

    def pop_back(self):
        self.check_empty()
        value = self.buffer[self.back]
        self.back = (self.back - 1) % self.size
        self.count -= 1
        return value


def run_all_commands(deque, commands):
    for command, *params in commands:
        try:
            result = getattr(deque, command)(*params)
            if result is not None:
                print(result)
        except AttributeError:
            raise ValueError(f"Неверная команда: {command}")
        except IndexError:
            print("error")


if __name__ == "__main__":
    command_count = int(input())
    run_all_commands(
        deque=Deque(int(input())),
        commands=(input().split() for _ in range(command_count)),
    )
