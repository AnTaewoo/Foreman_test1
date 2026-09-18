from convert import main


def test_main_converts_celsius_to_fahrenheit(capsys):
    result = main(["100", "--to", "f"])

    assert result == 0
    assert capsys.readouterr().out == "212.0\n"


def test_main_converts_fahrenheit_to_celsius(capsys):
    result = main(["32", "--to", "c"])

    assert result == 0
    assert capsys.readouterr().out == "0.0\n"


def test_main_converts_celsius_to_kelvin(capsys):
    result = main(["0", "--to", "k"])

    assert result == 0
    assert capsys.readouterr().out == "273.15\n"


def test_main_rounds_to_two_decimal_places(capsys):
    result = main(["1", "--to", "f"])

    assert result == 0
    assert capsys.readouterr().out == "33.8\n"


def test_main_reports_kelvin_value_error(capsys):
    result = main(["-273.16", "--to", "k"])

    assert result == 1
    assert capsys.readouterr().out.startswith("error: ")
