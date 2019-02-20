import pytest
from src.code import div

class TestDiv:

    @pytest.mark.parametrize("x, y, result", [
        (10, 2, 5),
        (10, 1, 10),
        (10, 10, 1)
    ])
    def test_div_zero_div(self, x, y, result):
        assert div(x, y) == result