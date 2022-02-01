import prog
import pytest 


@pytest.mark.parametrize("x,y,z",[(10,20,200),(20,30,9000)])
def test(x, y, z):
    assert x*y == z