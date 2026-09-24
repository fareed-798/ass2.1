from app import is_even, square
def test_square_positive_number():
    assert square(4) == 16
def test_square_negative_number():
    assert square(-3) == 
def test_is_even_even_number():
    assert is_even(8) is True
def test_is_even_odd_number():
    assert is_even(7) is False