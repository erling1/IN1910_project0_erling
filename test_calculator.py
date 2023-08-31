
import pytest
from calculator import add

#print(add(1,2))


def test_add(): 
    assert add(1,2) == 3

