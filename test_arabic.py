import pytest
from arabic_to_roman import convert_number


@pytest.mark.parametrize("test_input, expected", [
    (1, "I"),
    (5, "V"),
    (10, "X"),
    (50, "L"),
    (100, "C"),
    (500, "D"),
    (1000, "M")
])
def test_basic_assumptions(test_input, expected):
    assert convert_number(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    (11, "XI"),
    (54, "LIV"),
    (110, 'CX'),
    (123, "CXXIII"),
    (3450, "MMMCDL"),
    (2389, "MMCCCLXXXIX"),
    (504, 'DIV')
])
def test_convert_number(test_input, expected):
    assert convert_number(test_input) == expected


@pytest.mark.parametrize("test_input", [0, -5, 4000, 4567])
def test_out_of_range(test_input):
    with pytest.raises(ValueError):
        convert_number(test_input)
