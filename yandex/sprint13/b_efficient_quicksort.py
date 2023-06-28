# contest ID 88422702
def quick_sort(array):
    def partition(low, high):
        pivot = array[high]
        smaller_index = low - 1
        for current_index in range(low, high):
            if array[current_index] < pivot:
                smaller_index += 1
                array[smaller_index], array[current_index] = (
                    array[current_index],
                    array[smaller_index],
                )
        array[smaller_index + 1], array[high] = (
            array[high],
            array[smaller_index + 1],
        )
        return smaller_index + 1

    def quick_sort_rec(low, high):
        if low < high:
            pivot_index = partition(low, high)
            quick_sort_rec(low, pivot_index - 1)
            quick_sort_rec(pivot_index + 1, high)

    quick_sort_rec(0, len(array) - 1)
    return array


if __name__ == "__main__":

    class Participant:
        def __init__(self, login: str, solved_tasks: str, penalty: str):
            self.login = login
            self.solved_tasks = int(solved_tasks)
            self.penalty = int(penalty)

        def __lt__(self, other):
            if self.solved_tasks > other.solved_tasks:
                return True
            if self.solved_tasks < other.solved_tasks:
                return False
            if self.penalty < other.penalty:
                return True
            if self.penalty > other.penalty:
                return False
            return self.login < other.login

        def __str__(self):
            return self.login

    print(
        *quick_sort(
            [Participant(*input().split()) for _ in range(int(input()))]
        ),
        sep='\n'
    )
