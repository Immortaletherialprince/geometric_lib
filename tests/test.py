import pytest
import sys
sys.path.append('/home/egor/geometric_lib')
from calculate import calc
import math
def test_calc_circle_area():
    a = "circle"
    b = "area"
    c = [3]
    result = calc(a, b, c)
    assert result == math.pi*3*3

def test_calc_square_area():
    a = "square"
    b = "area"
    c = [4]
    result = calc(a, b, c)
    assert result == 16

def test_calc_circle_perimeter():
    a = "circle"
    b = "perimeter"
    c = [4]
    result = calc(a, b, c)
    assert result == 2* math.pi * 4

def test_calc_square_perimeter():
    a = "square"
    b = "perimeter"
    c = [5]
    result = calc(a, b, c)
    assert result == 20

def test_calc_invalid_function():
    a ="circle"
    b = "zzz"
    c = [3]
    with pytest.raises(AssertionError):
        calc(a, b, c)

def test_calc_invalid_figure():
    a = "zzz"
    b = "area"
    c = [3]
    with pytest.raises(AssertionError):
        calc(a, b, c)
