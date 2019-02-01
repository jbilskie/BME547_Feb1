import pytest
@pytest.mark.parametrize("a, b, expected", [
                                (2, 3, 5),
                                (5, -2, 3),
                                (10, 20, 30),
                                (20, 30, 50),
                                ])
def test_add(a,b,expected):
    from functions import add_two
    
    answer = add_two(a,b)
    assert answer == expected
