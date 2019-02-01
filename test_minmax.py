import pytest
@pytest.mark.parametrize("list, e_min, e_max", [
                                ([1,2,3,4,5,6],1,6),
                                ([6,5,4,3,2,1],1,6),
                                ([2,4,6,1,3,5],1,6),
                                ([5,1,6,3,4,2],1,6),
                                ])

def test_min_max(list,e_min,e_max):
    from functions import min_find
    from functions import max_find
    
    answer = min_find(list)
    assert answer == e_min
    answer = max_find(list)
    assert answer == e_max
