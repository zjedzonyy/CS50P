from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
