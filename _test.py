import prog 
import pytest 

@pytest.mark.one
def test_func():
    x = prog.func(3)
    assert x == 8

@pytest.mark.two
def test_method():
    x= prog.func(3)
    assert x ==7