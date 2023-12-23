import pytest
from Are_You_Playing_Banjo import are_you_playing_banjo


def test_are_you_playing_banjo():
    assert are_you_playing_banjo("martin") == "martin does not play banjo"
    assert are_you_playing_banjo("Rikke") == "Rikke plays banjo"
    assert are_you_playing_banjo("bravo") == "bravo does not play banjo"
    assert are_you_playing_banjo("rolf") == "rolf plays banjo"

