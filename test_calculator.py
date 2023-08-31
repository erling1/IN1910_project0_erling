
import pytest
from calculator import add

#print(add(1,2))

tol=1e-9

@pytest.mark.parametrize("test_input1, test_input2 , expected",[(1,2,3), (2,3,5),(3,4,7)])

def test_add(test_input1, test_input2 , expected): 
    assert add(test_input1,test_input2) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected",[(0.1,0.2,0.3), (0.2,0.3,0.5),(0.3,0.4,0.7)])

def test_float(test_input1, test_input2 , expected):
    assert abs(add(test_input1,test_input2) - expected) < tol
    

