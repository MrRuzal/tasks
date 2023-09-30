# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5
# litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres
# Nathan will drink, rounded to the smallest value.

import pytest

def test_litres_whole_number():
    assert litres(3) == 1

def test_litres_decimal_number():
    assert litres(6.7) == 3

def test_litres_large_number():
    assert litres(11.8) == 5

def test_litres_zero():
    assert litres(0) == 0

def test_litres_negative_number():
    assert litres(-2) == -1  # Should be rounded to -1


def litres(time):
    result = time // 2
    return result

if __name__ == '__main__':
    pytest.main()