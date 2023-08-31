
import pytest
from calculator import add

#print(add(1,2))

tol=1e-9

def test_add(): 
    assert add(1,2) == 3
    assert abs(add(0.1,0.2) - 0.3) < tol

