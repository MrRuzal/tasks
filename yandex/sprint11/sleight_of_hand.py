# contest ID 87713065
import collections
from typing import Iterable


def calculate_score(
    one_player_buttons: int,
    buttons: Iterable,
    players_count: int = 2,
    extra_characters='.',
) -> int:
    return sum(
        count <= one_player_buttons * players_count
        for value, count in collections.Counter(buttons).items()
        if value != extra_characters
    )


if __name__ == '__main__':
    print(
        calculate_score(
            one_player_buttons=int(input()),
            buttons=input() + input() + input() + input(),
        )
    )
