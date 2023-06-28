from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    """
    Функция get_weather_randomness вычисляет хаотичность погоды на основе
    ежедневных показаний температуры.
    Аргументы:
    - temperatures (List[int]): Список ежедневных показаний температуры.
    Возвращает:
    - int: Хаотичность погоды за данный период.
    Пример использования:
    >>> temperatures = [1, 2, 5, 4, 8]
    >>> result = get_weather_randomness(temperatures)
    >>> print(result)
    2
    """
    n = len(temperatures)
    chaotic_days = 0
    if n == 1:
        return 1
    for i in range(1, n - 1):
        # Проходим по каждому показанию температуры, кроме первого и последнего
        if (
            temperatures[i] > temperatures[i - 1]
            and temperatures[i] > temperatures[i + 1]
        ):
            chaotic_days += 1
        # Если температура текущего дня больше температуры
        # предыдущего и следующего дней,
        # то текущий день считается хаотичным
    if temperatures[0] > temperatures[1]:
        chaotic_days += 1
        # Проверяем первый день: если его температура больше температуры
        # второго дня, то он считается хаотичным
    if temperatures[n - 1] > temperatures[n - 2]:
        chaotic_days += 1
        # Проверяем последний день: если его температура больше
        # температуры предпоследнего дня, то он считается хаотичным
    return chaotic_days


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
