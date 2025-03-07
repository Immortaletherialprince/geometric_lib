import pytest
import sys
import math
from calculate import calc


sys.path.append('/home/egor/geometric_lib')


def test_calc_circle_area():
    fig = "circle"
    func = "area"
    size = [3]

    result = calc(fig, func, size)

    assert result == math.pi * 3 * 3


def test_calc_square_area():
    fig = "square"
    func = "area"
    size = [4]

    result = calc(fig, func, size)

    assert result == 16


def test_calc_circle_perimeter():
    fig = "circle"
    func = "perimeter"
    size = [4]

    result = calc(fig, func, size)

    assert result == 2 * math.pi * 4


def test_calc_square_perimeter():
    fig = "square"
    func = "perimeter"
    size = [5]

    result = calc(fig, func, size)

    assert result == 20


def test_calc_invalid_function():
    fig = "circle"
    func = "zzz"
    size = [3]

    with pytest.raises(AssertionError):
        calc(fig, func, size)


def test_calc_invalid_figure():
    fig = "zzz"
    func = "area"
    size = [3]

    with pytest.raises(AssertionError):
        calc(fig, func, size)


def test_calc_invalid_size():
    fig = "circle"
    func = "area"
    size = [-3]

    with pytest.raises(ValueError):
        calc(fig, func, size)
