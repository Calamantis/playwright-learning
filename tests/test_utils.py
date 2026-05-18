import pytest

from utils import calculate_brutto

def test_calculate_brutto_standard():
    assert calculate_brutto(100) == 123.00

def test_calculate_brutto_custom_vat():
    assert calculate_brutto(100, 0.08) == 108.00

def test_calculate_brutto_negative_value():
    with pytest.raises(ValueError, match="Cena netto nie może być ujemna"):
        calculate_brutto(-10)

#TDD?
@pytest.mark.parametrize("netto, vat, expected", [
    (100, 0.23, 123.00),
    (50, 0.08, 54.00),
    (0, 0.23, 0.00),
    (10.50, 0.23, 12.91)
])
def test_calculate_brutto_multiple_cases(netto, vat, expected):
    assert calculate_brutto(netto, vat) == expected


def test_letter_input():
    with pytest.raises(TypeError) as excinfo:
        calculate_brutto("sto złotych")
    assert "Cena netto musi być liczbą" in str(excinfo.value) # this assert guarantees the functions error message

def test_float_input():
        assert calculate_brutto(1.0) == 1.23

