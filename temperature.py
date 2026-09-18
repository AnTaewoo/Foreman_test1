def c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero")
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def c_to_k(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero")
    return celsius + 273.15
