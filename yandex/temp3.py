from dataclasses import dataclass


def quick_sort(array: list):
    def partition(low: int, high: int):
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

    def quick_sort_rec(low: int, high: int):
        if low < high:
            pivot_index = partition(low, high)
            quick_sort_rec(low, pivot_index - 1)
            quick_sort_rec(pivot_index + 1, high)

    quick_sort_rec(0, len(array) - 1)
    return array


@dataclass
class Participant:
    login: str
    solved_tasks: int
    penalty: int

    def __lt__(self, other):
        return (-self.solved_tasks, self.penalty, self.login) < (
            -other.solved_tasks,
            other.penalty,
            other.login,
        )

    def __str__(self):
        return self.login


def create_participant(
    login: str, solved_tasks: int, penalty: int
) -> Participant:
    return Participant(login, int(solved_tasks), int(penalty))


if __name__ == "__main__":
    print(
        *quick_sort(
            [create_participant(*input().split()) for _ in range(int(input()))]
        ),
        sep='\n'
    )
