
import pytest
from calculator import add, divide, factorial, sin, mean, var

#print(add(1,2))

tol=1e-9

@pytest.mark.parametrize("test_input1, test_input2 , expected",[(1,2,3), (2,3,5),(3,4,7)])

def test_add(test_input1, test_input2 , expected): 
    assert add(test_input1,test_input2) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected",[(0.1,0.2,0.3), (0.2,0.3,0.5),(0.3,0.4,0.7)])

def test_float(test_input1, test_input2 , expected):
    assert abs(add(test_input1,test_input2) - expected) < tol
    

@pytest.mark.parametrize("test_input1, test_input2, expected",[(1,2,0.5), (2,3,5),(3,4,7)])

def test_divide(test_input1, test_input2, expected):
    assert divide(test_input1,test_input2) == expected


@pytest.mark.parametrize("test_input1, expected",[(10,100), (2,3),(3,7)])

def test_factorial(test_input1,  expected):
    assert factorial(test_input1) == expected

@pytest.mark.parametrize("test_input1, expected",[(0,0), (0.2,0.3),(0.3,0.7)])

def test_sin(test_input1,expected):
    assert sin(test_input1) == expected

x_list1 = [1,2,3,4,5,6,7,2,4,56,7]
x_list2 = [2,3,4,6,7,4,5,76,4,]
x_list3 = [2,3,45,3,2,4,3,5,6,4,4,3,5]

@pytest.mark.parametrize("test_input1, expected",[(x_list1, 5), (x_list2,4),(x_list3,4)])

def test_mean(test_input1, expected):
    assert mean(test_input1) == expected

@pytest.mark.parametrize("test_input1, expected",[(x_list1, 5), (x_list2,4),(x_list3,4)])
                         
def test_var(test_input1, expected):
    assert var(test_input1) == expected