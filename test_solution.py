from solution import Solution
import pytest


@pytest.fixture
def solution():
    return Solution()


def test1(solution: Solution):
    assert solution.romanToInt("III") == 3


def test2(solution: Solution):
    assert solution.romanToInt("LVIII") == 58


def test3(solution: Solution):
    assert solution.romanToInt("MCMXCIV") == 1994
