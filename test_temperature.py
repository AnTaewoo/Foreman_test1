import pytest

from temperature import c_to_f, c_to_k, f_to_c


def test_c_to_f_converts_celsius_to_fahrenheit():
    assert c_to_f(100) == 212.0
    assert c_to_f(0) == 32.0


def test_f_to_c_converts_fahrenheit_to_celsius():
    assert f_to_c(32) == 0.0
    assert f_to_c(212) == 100.0


def test_c_to_k_converts_celsius_to_kelvin():
    assert c_to_k(0) == 273.15
    assert c_to_k(-273.15) == 0.0


def test_c_to_k_rejects_values_below_absolute_zero():
    with pytest.raises(ValueError):
        c_to_k(-273.16)
