import mathematics.trigonometry as trig
from math import isclose
import pytest

# object oriented way of testing
class TestTrignometry:

    def test_factorial(self):
        assert trig.factorial(5) == 120

    @pytest.mark.skip(reason="This feature is under development")
    def test_sec(self):
        assert False




#procedural way

def test_cosine():
    """Test the cosine function."""
    assert isclose(trig.cosine(0), 1, abs_tol=1e-6)
    
