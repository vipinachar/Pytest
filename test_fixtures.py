import prog
import pytest 

@pytest.fixture
def numbers():
    array = [5,10,20]
    return array 


def test_func(numbers):
    assert numbers[0] == 5

def test_func_2(numbers):
    assert numbers[1] == 10

def test_func_3(numbers):
    assert numbers[2] == 20
